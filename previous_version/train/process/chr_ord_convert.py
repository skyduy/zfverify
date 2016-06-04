# coding: utf-8

"""
    ...
    ~~~~~~~~~~

    :author Skyduy <cuteuy@gmail.com> <http://skyduy.me>

"""

answers = ['1', '0', '3', '2', '5', '4', '7', '6', '9', '8', 'a', 'c', 'b', 'e', 'd', 'g', 'f', 'i', 'h', 'k', 'j', 'm',
           'l', 'n', 'q', 'p', 's', 'r', 'u', 't', 'w', 'v', 'y', 'x']
answers = sorted(answers)
print answers

answers = map(lambda x: x - 48 if x <= 57 else x - 87 if x <= 110 else x - 88, map(ord, answers))
print answers


answers = map(chr, map(lambda x: x + 48 if x <= 9 else x + 87 if x <= 23 else x+88, map(int, answers)))
print answers
