#-*- coding:utf-8 -*-
import os
import Image

whereopen=os.getcwd()+'/tests/' 
wheresave=os.getcwd()+'/tests/sigle/' 


def ismovepoint(im,width,height):
    pixel = []
    try:
        pixel.append(im.getpixel((width, height-1)))
        pixel.append(im.getpixel((width, height+1)))
        pixel.append(im.getpixel((width+1, height)))
        pixel.append(im.getpixel((width-1, height)))
        pixel.append(im.getpixel((width-1, height-1)))
        pixel.append(im.getpixel((width-1, height+1)))
        pixel.append(im.getpixel((width+1, height-1)))
        pixel.append(im.getpixel((width+1, height+1)))  
    except Exception:
        return True
    else:
        for term in pixel:
            if term > 30:
                pass
            else:
                break 
        else:
            return True
        return False


def to0and1(im):
    width, height = im.size
    for h in range(0, height):  
        for w in range(0, width): 
            pixel = im.getpixel((w, h)) 
            if pixel <= 30 and not ismovepoint(im, w, h):
                pixel = 0
            else:
                pixel = 255 
            im.putpixel((w,h),pixel)
    return im


def splitimg(image):
    "Roll an image sideways"
    image = image.convert("L")
    xsize, ysize = image.size
    new = image.crop((4, 0, xsize-18, ysize))
    xsize, ysize = new.size
    lenth = xsize/4;
    part1 = new.crop((0, 0, lenth, ysize))
    part2 = new.crop((lenth, 0, 2*lenth, ysize))
    part3 = new.crop((2*lenth, 0, 3*lenth, ysize))
    part4 = new.crop((3*lenth, 0, 4*lenth, ysize))
    return part1,part2,part3,part4





for i in range(1,10):
    infile = whereopen + '%s.png' %i
    im = Image.open(infile)
    img = splitimg(im)
    to0and1(img[0]).save(wheresave+'%s01.png' %i)
    to0and1(img[1]).save(wheresave+'%s02.png' %i)
    to0and1(img[2]).save(wheresave+'%s03.png' %i)
    to0and1(img[3]).save(wheresave+'%s04.png' %i)


