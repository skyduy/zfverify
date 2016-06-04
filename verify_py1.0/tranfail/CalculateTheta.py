# coding: utf-8
from numpy import loadtxt, savetxt
from numpy import mean, shape, transpose
from numpy import matrix
from oneVsAll import oneVsAll
from predictOneVsAll import predictOneVsAll

def ccTheta():
    """
        测试成功
    """

    input_layer_size  = 324
    num_labels = 36

    X = matrix(loadtxt('./SampleDATA/X.dat'))
    y = matrix(loadtxt('./SampleDATA/y.dat')).transpose()
    the_lambda = 0.1

    all_theta = oneVsAll(X, y, num_labels, the_lambda)
    savetxt('theta.dat',all_theta)

    Accuracy, pred = predictOneVsAll(all_theta, X)

    print '\nTraining Set Accuracy: \n',   pred == y

    return all_theta