# coding: utf-8
from numpy import matrix
from oneVsAll import oneVsAll
from numpy import loadtxt, savetxt
from predictOneVsAll import predictOneVsAll


def train():
    num_labels = 34

    print '... Training'
    X = matrix(loadtxt('X.dat')) / 255.0
    y = matrix(loadtxt('y.dat')).transpose()
    the_lambda = 0.1
    all_theta = oneVsAll(X, y, num_labels, the_lambda)
    savetxt('theta.dat', all_theta)


def test():
    print '... Testing'
    all_theta = matrix(loadtxt('theta.dat'))
    X_test = matrix(loadtxt('X_test.dat')) / 255.0
    y_test = matrix(loadtxt('y_test.dat')).transpose()
    acc, pred = predictOneVsAll(all_theta, X_test)
    single_acc = sum(pred == y_test) / (len(y_test) * 1.0)
    max_acc = pow(single_acc, 4)
    min_acc = single_acc*4 - 3
    print 'Theoretical accuracy:'
    print '\tSingle accuracy: %2.2f%%' % (single_acc*100)
    print '\tTotal accuracy: %2.2f%% ~ %2.2f%%' % (min_acc*100, max_acc*100)


test()
