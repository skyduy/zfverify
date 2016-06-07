# 正方验证码识别工具
## 简单使用[Sklearn](http://scikit-learn.org/)实现。
### 注：因为训练样本为正方验证码，故该工具只适合正方验证码识别
    这里有两种测试方式在predict.py向verify函数传递save参数决定。
        1. 保存验证码之后验证,可以验证结果。
        2. 直接预测,多并发使用，速度快。
###cache

    验证码获取临时保存位置
    
###model

    重要目录，训练模型文件存储位置

###train

    训练目录，训练代码

###predict.py
    
    接口文件， 传入相应参数，返回识别结果

* Copyright
  * Do not for commercial.(If you must do, please contact me.)