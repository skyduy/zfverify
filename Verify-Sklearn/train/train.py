# coding: utf-8

from PIL import Image
import numpy as np
from sklearn import svm
from sklearn.externals import joblib
from sklearn.cross_validation import train_test_split


def load_data():
    kv_dict = {}
    with open('answer.txt') as f:
        for pre, answers in enumerate(f):
            answers = answers.strip()
            answers = map(lambda x: x - 48 if x <= 57 else x - 87 if x <= 110 else x - 88, map(ord, answers))
            for i, v in enumerate(answers):
                kv_dict['%s-%d.png' % (pre, i)] = v

    folder = 'sample_single'
    imgs = kv_dict.keys()
    length = len(imgs)
    data = np.empty((length, 21 * 16), dtype="float32")
    label = np.empty(length)
    for index, img_name in enumerate(imgs):
        img = Image.open('%s/%s' % (folder, img_name))
        data[index, :] = np.asarray(img, dtype="float32").flatten() / 255.0
        label[index] = kv_dict[img_name]
    return data, label


def train(data, target, model_save):
    classifier = svm.LinearSVC()
    classifier.fit(data, target)
    joblib.dump(classifier, model_save)


if __name__ == '__main__':
    model_file = '../model/zf_linearSVC.pkl'
    print '... loading data'
    x_data, y_data = load_data()

    print '... training'
    X_train, X_test, y_train, y_test = train_test_split(x_data, y_data, test_size=0.1, random_state=0)
    train(X_train, y_train, model_file)

    print '... testing'
    clf = joblib.load(model_file)
    answer = clf.predict(X_test)
    single_acc = sum(y_test == answer) * 1.0 / len(answer)
    max_acc = pow(single_acc, 4)
    min_acc = single_acc*4 - 3
    print 'Theoretical accuracy:'
    print '\tSingle accuracy: %2.2f%%' % (single_acc*100)
    print '\tTotal accuracy: %2.2f%% ~ %2.2f%%' % (min_acc*100, max_acc*100)
