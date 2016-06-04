# coding:utf-8
import urllib
from PIL import Image


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
    data_file = 'X.dat'
    pic_name = 'tmp/todo.png'
    urllib.urlretrieve(url, pic_name)
    get_single(pic_name)

    # saveindata(newpath, names, data_file)

    print 'OK! It\'s time to predict the picture.'

if __name__ == '__main__':
    verify('http://jwxt.jit.edu.cn/CheckCode.aspx')
