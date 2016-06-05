# coding: utf-8

import os
from PIL import Image


def img2single(samples_folder, single_folder):
    imgs = os.listdir(samples_folder)
    for img in imgs:
        image = Image.open('%s/%s' % (samples_folder, img)).convert("L")
        x_size, y_size = image.size
        y_size -= 5
        # y from 1 to y_size-5
        # x from 4 to x_size-18
        piece = (x_size-22) / 8
        centers = [4+piece*(2*i+1) for i in range(4)]
        pre = img.split('.')[0]
        for i, center in enumerate(centers):
            image.crop((center-(piece+2), 1, center+(piece+2), y_size)).save('%s/%s-%s.png' % (single_folder, pre, i))


img2single('../samples', '../sample_single')
