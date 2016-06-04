# coding:utf-8
"""
    获取验证码样例
"""
import os  

filepath=os.getcwd()+'/tmp'
for x in range(108,301):
    temp= filepath + '/%s.aspx' % x
    temp2 = filepath + '/%s.png' % x
    os.rename(temp, temp2)

print '图片下载完毕，保存路径为'+filepath

