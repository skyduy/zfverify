#-*- coding:utf-8 -*-
import os
import Image

whereopen = os.getcwd()+'/samples/' 
wheresave = os.getcwd()+'/samples/Ydata/'

infile = whereopen + 'answer.txt'
outfile = wheresave + 'Y.dat'

def saveY(i,line):
    for j in range(1,5):
        thefile = open(outfile,'a')
        number = ord(line[j-1])
        rownum = getRow(number)
        print >> thefile, rownum
        thefile.close()

def getRow(number):
    if number >= 48 and number <= 57:
        return number - 48
    else:
        return number - 87


linenum = 1
for line in open(infile):
    saveY(linenum,line)
    linenum = linenum + 1

