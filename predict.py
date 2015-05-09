# coding: utf-8

import urllib
import os
import urllib2
from PIL import Image
from cStringIO import StringIO
from sklearn.externals import joblib


def img2single(infile, where_save):
    images = []
    raw_img = Image.open(infile).convert("L")
    x_size, y_size = raw_img.size
    y_size -= 5
    new = raw_img.crop((4, 1, x_size-18, y_size))
    x_size, y_size = new.size
    length = x_size/4
    for i in range(4):
        images.append(new.crop((i*length, 0, (i+1)*length, y_size)))
    for index, img in enumerate(images):
        img.save(where_save+'%s.png' % str(index+1))


def get_data(where_x_pics):
    pic_data = []

    for j in range(4):
        pic_file = where_x_pics + '%s.png' % str(j+1)
        im = Image.open(pic_file)
        width, height = im.size
        result = []
        for h in range(0, height):
            for w in range(0, width):
                pixel = im.getpixel((w, h))
                result.append(pixel)
        pic_data.append(result)
    return pic_data


def verify_and_save(url, model, save_path):
    """

    :param url: 验证码地址
    :param model: 处理该验证码的模型
    :param save_path: 存放验证码的目录
    :return:
    """
    pic_file = save_path + 'todo.png'
    urllib.urlretrieve(url, pic_file)
    img2single(pic_file, save_path)

    data = get_data(save_path)
    clf = joblib.load(model)
    raw_data = clf.predict(data)
    result = map(chr, map(lambda x: x+48 if 0 <= x <= 9 else x+87, map(int, raw_data)))

    return result


def verify_without_save(url, model):
    pic_data = []
    f = StringIO(urllib2.urlopen(url).read())
    raw_img = Image.open(f)
    x_size, y_size = raw_img.size
    y_size -= 5
    new = raw_img.crop((4, 1, x_size-18, y_size))
    x_size, y_size = new.size
    length = x_size/4
    for i in range(4):
        im = new.crop((i*length, 0, (i+1)*length, y_size))
        width, height = im.size
        result = []
        for h in range(0, height):
            for w in range(0, width):
                pixel = im.getpixel((w, h))
                result.append(pixel)
        pic_data.append(result)

    clf = joblib.load(model)
    raw_data = clf.predict(pic_data)
    result = map(chr, map(lambda x: x+48 if 0 <= x <= 9 else x+87, map(int, raw_data)))

    return result


if __name__ == '__main__':
    the_url = 'http://jwxt.jit.edu.cn/CheckCode.aspx'
    the_model = os.getcwd() + '/model/zf_linearSVC.pkl'
    the_save_path = os.getcwd() + '/cache/'

    print verify_and_save(the_url, the_model, the_save_path)

    print verify_without_save(the_url, the_model)