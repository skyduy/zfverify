# 正方验证码识别工具
## 使用Octave，从最底层实现验证码识别.
### 注：因为训练样本为正方验证码，故该工具只适合正方验证码识别

    优化方式为fmincg，源码为train/core/fmincg.m for Coursera Machine learning.

    使用方法：
        0、train/split_imgs.py get_dat.py进行数据获取，手动将X分为X和X_test，对应的y也相应分。
        1、train/core/train.m 反注释掉上一部分，注释掉下一部分，运行进行训练
        2、更改train/core/theta.m，删除被注释的部分
        3、train/core/train.m 注释掉上一部分，反注释掉下一部分，运行进行测试
        4、将train/core/theta.dat复制到predict/目录下
        5、运行predict/prepare.py准备待识别数据
        6、运行predict/verify.m进行识别

* Copyright
  * OpenSource now.
  * Do not for commercial.(If you must do, please contact me.)