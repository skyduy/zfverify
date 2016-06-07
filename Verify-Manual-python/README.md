# 正方验证码识别工具
## 使用[Numpy](http://www.numpy.org/), [Scipy](https://www.scipy.org/)，从底层实现验证码识别
### 注：因为训练样本为正方验证码，故该工具只适合正方验证码识别

    优化方式为scipy.optimize.fmin_bfgs

    使用方法：
        0、train/split_imgs.py get_dat.py进行数据获取，手动将X分为X和X_test，对应的y也相应分。
        1、train/core/train.py 中train和test函数分别用于训练和测试
        4、将train/core/theta.dat复制到predict/目录下
        6、运行predict/verify.py进行识别

* Copyright
  * OpenSource now.
  * Do not for commercial.(If you must do, please contact me.)