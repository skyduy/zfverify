# coding: utf-8

import urllib
import urllib2
import numpy as np
from PIL import Image
from cStringIO import StringIO
from sklearn.externals import joblib


def verify(url, model, save=False):
    """
    :param url: 验证码地址
    :param model: 处理该验证码的模型
    :param save: 是否保存临时文件到cache
    :return:
    """
    if save:
        pic_file = 'cache/todo.png'
        urllib.urlretrieve(url, pic_file)
        image = Image.open(pic_file).convert("L")
    else:
        image = Image.open(StringIO(urllib2.urlopen(url).read()))
    x_size, y_size = image.size
    y_size -= 5

    # y from 1 to y_size-5
    # x from 4 to x_size-18
    piece = (x_size-22) / 8
    centers = [4+piece*(2*i+1) for i in range(4)]
    data = np.empty((4, 21 * 16), dtype="float32")
    for i, center in enumerate(centers):
        single_pic = image.crop((center-(piece+2), 1, center+(piece+2), y_size))
        data[i, :] = np.asarray(single_pic, dtype="float32").flatten() / 255.0
        if save:
            single_pic.save('cache/todo-%s.png' % i)
    clf = joblib.load(model)
    answers = clf.predict(data)
    answers = map(chr, map(lambda x: x + 48 if x <= 9 else x + 87 if x <= 23 else x + 88, map(int, answers)))
    return answers

if __name__ == '__main__':
    the_url = 'http://jwxt.jit.edu.cn/CheckCode.aspx'
    the_model = 'model/zf_linearSVC.pkl'
    print verify(the_url, the_model)
    print verify(the_url, the_model, save=True)
