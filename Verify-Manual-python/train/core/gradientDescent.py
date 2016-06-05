# coding: utf-8
from numpy import matrix, array
from numpy import sum
from numpy import zeros

from sigmoid import sigmoid


def lrGD(theta, *args):
    theta = matrix(theta).transpose()
    X, y, the_lambda = args
    m = y.shape[0]
    grad = zeros(theta.shape)

    htheta = sigmoid(X * theta)
    grad[0] = 1.0/m * sum(array((htheta-y))*array(X[:, 0:1]))
    for i in range(1, theta.shape[0]):
        grad[i] = 1.0/m * sum(array((htheta-y))*array(X[:, i:i+1])) + the_lambda/m*theta[i]
    return grad.flatten()
