# coding: utf-8
from numpy import shape, hstack, transpose, matrix
from numpy import ones, zeros
from scipy.optimize import fmin_bfgs
from lrCostFunction import lrCostFunction
from gradientDescent import lrGD

def oneVsAll(X, y, num_labels, the_lambda):
    """
        用fmin_cg没搞定。最后还是用的fmin_bfgs
    """
    m = shape(X)[0]
    n = shape(X)[1]

    all_theta = matrix(zeros((num_labels, n+1)))
    X = hstack((ones((m, 1)), X))
    for c in range(num_labels):
        initial_theta = zeros((n+1, 1))
        args = (X, (y == c), the_lambda)
        theta = fmin_bfgs(lrCostFunction, initial_theta, fprime=lrGD, args=args)
        all_theta[c:c+1,:] = theta.transpose()

    return all_theta