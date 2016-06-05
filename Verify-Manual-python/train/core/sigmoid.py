# coding: utf-8
from numpy import exp


def sigmoid(z):
    g = 1.0/(1.0+exp(-z))
    return g
