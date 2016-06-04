# coding:utf-8
"""
    获取验证码样例
"""
import re  
import string  
import sys  
import os  
import urllib  
import Image


def savepic(url, savepath, picname):
    if not os.path.exists(savepath):  
        os.mkdir(savepath)  
    pic= savepath + picname
    urllib.urlretrieve(url,pic)

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

def handlepic(filepath, picname):
    newpath = filepath + 'sigles/'
    if not os.path.exists(newpath):  
            os.mkdir(newpath)  

    newname = ['1.png','2.png','3.png','4.png'];

    infile = filepath + picname
    im = Image.open(infile)
    imgs = splitimg(im)
    for i in range(4):
        to0and1(imgs[i]).save(newpath+newname[i])
    return newpath, newname

def saveindata(filepath, names, datname):
    datfile = filepath + datname
    thefile = open(datfile,'w')
    for term in names:
        infile = filepath + term
        im = Image.open(infile)
        width, height = im.size
        for h in range(0, height):  
            for w in range(0, width):  
                pixel = im.getpixel((w, h))   
                print >> thefile, pixel,
        print >> thefile, ''
    thefile.close()

def verify(url):
    """
    输入图片URL，返回该图片的值，仅限正方验证码图片
    """
    filepath=os.getcwd()+'/Data/'
    picname = 'todo.png'
    datname = 'X.dat'

    savepic(url, filepath, picname)
    newpath, names = handlepic(filepath, picname)
    saveindata(newpath, names, datname)

    print 'OK! It\'s time to predict the picture.'

if __name__ == '__main__':
    verify('http://jwxt.jit.edu.cn/CheckCode.aspx')