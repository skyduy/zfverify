from numpy import loadtxt
from numpy import matrix, shape
from predictOneVsAll import predictOneVsAll


def predict(Xfile, thetafile):
    X = matrix(loadtxt('./Data/sigles/X.dat'))
    theta = matrix(loadtxt('./Data/theta.dat'))

    result = []

    for i in range(4):
        pred = predictOneVsAll(theta, X[i,:])
        num = pred[1]
        if num >= 0 and num <=9:
            ascii_code = num + 48
        else:
            ascii_code = num + 87
        result.append(chr(ascii_code))
    return result

