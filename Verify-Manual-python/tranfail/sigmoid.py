# coding: utf-8
from numpy import exp
def sigmoid(z):
    """
        S值计算，测试成功
    """
    g = 1.0/(1.0+exp(-z))
    return g