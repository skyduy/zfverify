# coding: utf-8
from numpy import log, sum
from numpy import array, matrix

from sigmoid import sigmoid


def lrCostFunction(theta, *args):
    theta = matrix(theta).transpose()
    X, y, the_lambda = args
    m = y.shape[0]
    htheta = sigmoid(X*theta)
    J = -sum(array(y)*array(log(htheta)) + array((1-y))*array(log(1-htheta)))/m + the_lambda*sum(array(theta[1:]) * array(theta[1:]))/(2*m)
    return J
