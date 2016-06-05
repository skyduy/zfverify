# coding: utf-8

"""
    ...
    ~~~~~~~~~~
    
    :author Skyduy <cuteuy@gmail.com> <http://skyduy.me>
    
"""
from PIL import Image


def char2num(char):
    t = ord(char)
    return (lambda x: x - 48 if x <= 57 else x - 87 if x <= 110 else x - 88)(t)


with open('core/X.dat', 'w') as x_file:
    with open('core/y.dat', 'w') as y_file:
        with open('answer.txt') as answer:
            for i, line in enumerate(answer):
                line = line.strip()
                for j, v in enumerate(line):
                    img = Image.open('sample_single/%s-%s.png' % (i, j))

                    width, height = img.size
                    for h in range(0, height):
                        for w in range(0, width):
                            pixel = img.getpixel((w, h))
                            print >> x_file, pixel,
                    print >> x_file, ''
                    print >> y_file, char2num(v)
