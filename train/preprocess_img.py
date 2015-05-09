# coding: utf-8

import os
from PIL import Image


def to0and1(image):
    width, height = image.size
    tmp = []
    for h in range(0, height):
        for w in range(0, width):
            pixel = image.getpixel((w, h))
            tmp.append(pixel)
            if pixel == 17 or pixel == 204:
                pixel = 0
            else:
                pixel = 255
            image.putpixel((w, h), pixel)
    return image


def split_img(image):
    image = image.convert("L")
    x_size, y_size = image.size
    y_size -= 5
    new = image.crop((4, 1, x_size-18, y_size))
    x_size, y_size = new.size
    length = x_size/4
    part1 = new.crop((0, 0, length, y_size))
    part2 = new.crop((length, 0, 2*length, y_size))
    part3 = new.crop((2*length, 0, 3*length, y_size))
    part4 = new.crop((3*length, 0, 4*length, y_size))
    return part1, part2, part3, part4


def img2single(where_open, where_save, num):
    for i in range(num):
        infile = where_open + '%s.png' % i
        im = Image.open(infile)
        img = split_img(im)
        for j in range(4):
            img[j].save(where_save+'%s-%s.png' % (i, j))
            # to0and1(img[i]).save(where_save+'0%s.png' % i+1)


if __name__ == '__main__':
    samples_open = os.getcwd() + '/samples/'
    samples_save = os.getcwd() + '/samples/single/'
    the_num = 300
    img2single(samples_open, samples_save, the_num)

    # tests_open = os.getcwd() + '/tests/'
    # tests_save = os.getcwd() + '/tests/single/'
    # the_num = 9
    # img2single(tests_open, tests_save, the_num)


