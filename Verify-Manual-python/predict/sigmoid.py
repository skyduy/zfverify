# coding: utf-8
from numpy import exp
def sigmoid(z):
    """
        返回S函数值
    """
    g = 1.0/(1.0+exp(-z))
    return g