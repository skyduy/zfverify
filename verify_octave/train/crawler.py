# coding:utf-8
"""
    获取验证码样例
"""
import re  
import string  
import sys  
import os
import time
import urllib  
  
url="http://jwxt.jit.edu.cn/CheckCode.aspx"
filepath=os.getcwd()+'/tmp'
    
if os.path.exists(filepath) is False:  
    os.mkdir(filepath)  


print u'getting imgs...'  
for x in range(221,301):
    temp= filepath + '/%s.aspx' % x
    time.sleep(1)
    print u'正在下载第%s张图片' % x  
    urllib.urlretrieve(url,temp)  

print '图片下载完毕，保存路径为'+filepath