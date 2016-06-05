# coding: utf-8
from numpy import dot, hstack, ones, argmax
from sigmoid import sigmoid


def predictOneVsAll(all_theta, X):
    m = X.shape[0]

    X = hstack((ones((m, 1)), X))

    real_all_theta = all_theta.transpose()
    all_predict = sigmoid(dot(X, real_all_theta))

    acc = all_predict.max(1)
    p = argmax(all_predict, axis=1)

    return acc, p

