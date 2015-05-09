# coding: utf-8

import os
from PIL import Image
from pandas import DataFrame


def data2csv(where_x_pics, where_y_ans, saved_file):
    answers = []
    pic_data = []
    all_data = {}

    answer_file = where_y_ans + 'answer.txt'
    with open(answer_file, 'r') as f:
        for index, line in enumerate(f):
            for j in range(4):
                number = ord(line[j])
                answers.append(number)

                pic_file = where_x_pics + '%s-%s.png' % (index, j)
                im = Image.open(pic_file)
                width, height = im.size
                result = []
                for h in range(0, height):
                    for w in range(0, width):
                        pixel = im.getpixel((w, h))
                        result.append(pixel)
                pic_data.append(result)

    all_data['pic_data'] = pic_data
    answers = map(lambda t: t-48 if 48 <= t <= 57 else t-87, answers)
    all_data['answers'] = answers

    DataFrame(all_data, columns=['pic_data', 'answers']).to_csv(saved_file)

if __name__ == '__main__':
    samples_x_open = os.getcwd() + '/samples/single/'
    samples_y_open = os.getcwd() + '/samples/'
    samples_csv = os.getcwd() + '/samples/data/data.csv'
    data2csv(samples_x_open, samples_y_open, samples_csv)

    # tests_x_open = os.getcwd() + '/tests/single/'
    # tests_y_open = os.getcwd() + '/tests/'
    # tests_csv = os.getcwd() + '/tests/data/data.csv'
    # data2csv(tests_x_open, tests_y_open, tests_csv)