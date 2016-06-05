# coding: utf-8
from numpy import shape, hstack, matrix
from numpy import ones, zeros
from scipy.optimize import fmin_bfgs
from lrCostFunction import lrCostFunction
from gradientDescent import lrGD


def oneVsAll(X, y, num_labels, the_lambda):
    m, n = shape(X)
    all_theta = matrix(zeros((num_labels, n+1)))
    X = hstack((ones((m, 1)), X))
    for c in range(num_labels):
        print 'Training for %d/34' % (c+1)
        initial_theta = zeros((n+1, 1))
        args = (X, (y == c), the_lambda)
        theta = fmin_bfgs(lrCostFunction, initial_theta, fprime=lrGD, args=args, maxiter=50)
        all_theta[c, :] = theta.transpose()

    return all_theta
