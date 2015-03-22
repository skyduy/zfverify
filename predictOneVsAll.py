# coding: utf-8
from numpy import shape, transpose
from numpy import dot, hstack, ones, argmax, max
from sigmoid import sigmoid

def predictOneVsAll(all_theta, X):
    """
        尚未测试
    """
    m = X.shape[0]

    X = hstack((ones((m, 1)), X))

    real_all_theta = all_theta.transpose()

    all_predict = sigmoid(X* real_all_theta)
    Accuracy = all_predict.max(1);
    p = argmax(all_predict, axis=1)
    
    return Accuracy, p

