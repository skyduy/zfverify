# coding: utf-8

import os
from sklearn.externals import joblib
from numpy import array
from pandas import read_csv
from sklearn import svm
from collections import Counter


def load_data(data_file, with_zip=False):
    data_frame = read_csv(data_file)
    pic_data = map(eval, data_frame['pic_data'])
    answers = list(data_frame['answers'])
    if with_zip:
        return zip(map(array, pic_data), answers)
    return array(map(array, pic_data)), array(answers)


def train(data, target, model_save):
    classifier = svm.LinearSVC()
    classifier.fit(data, target)
    joblib.dump(classifier, model_save)


if __name__ == '__main__':
    model_file = os.path.pardir+'/model/zf_linearSVC.pkl'
    print 'training ...'
    the_data_file = os.getcwd() + '/samples/data/data.csv'
    x_data, y_data = load_data(the_data_file)
    train(x_data, y_data, model_file)

    # print 'testing...'
    # test_data_file = os.getcwd() + '/samples/data/data.csv'
    # clf = joblib.load(model_file)
    # test_x, test_y = load_data(test_data_file)
    # length = len(test_x)
    # print Counter(test_y[length*0.75:] == clf.predict(test_x[length*0.75:]))


