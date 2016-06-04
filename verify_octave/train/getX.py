#-*- coding:utf-8 -*-
import os
import Image

whereopen = os.getcwd()+'/tests/sigle/' 
wheresave = os.getcwd()+'/tests/Xdata/'


datfile = wheresave + 'X.dat'
thefile = open(datfile,'a')
for i in range(1,10):
    for j in range(1,5):
        thefile = open(datfile,'a')
        infile = whereopen + '%s0%s.png' %(i, j)
        im = Image.open(infile)
        width, height = im.size
        for h in range(0, height):  
            for w in range(0, width):  
                pixel = im.getpixel((w, h))   
                print >> thefile, pixel,
        print >> thefile, ''
        thefile.close()