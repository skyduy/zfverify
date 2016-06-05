# coding: utf-8
import urllib
from PIL import Image
from numpy import matrix
from numpy import loadtxt
from predictOneVsAll import predictOneVsAll


def prepare_data(url):
    pic_file = 'cache/todo.png'
    urllib.urlretrieve(url, pic_file)
    with open('cache/X.dat', 'w') as x_file:
        image = Image.open(pic_file).convert("L")
        x_size, y_size = image.size
        y_size -= 5
        # y from 1 to y_size-5
        # x from 4 to x_size-18
        piece = (x_size-22) / 8
        centers = [4+piece*(2*i+1) for i in range(4)]
        for i, center in enumerate(centers):
            img = image.crop((center-(piece+2), 1, center+(piece+2), y_size))
            width, height = img.size
            for h in range(0, height):
                for w in range(0, width):
                    pixel = img.getpixel((w, h))
                    print >> x_file, pixel,
            print >> x_file, ''


def verify():
    prepare_data('http://jwxt.jit.edu.cn/CheckCode.aspx')
    all_theta = matrix(loadtxt('theta.dat'))
    X = matrix(loadtxt('cache/X.dat')) / 255.0
    acc, pred = predictOneVsAll(all_theta, X)
    answers = map(chr, map(lambda x: x + 48 if x <= 9 else x + 87 if x <= 23 else x + 88, pred))
    return ''.join(answers)

print verify()

