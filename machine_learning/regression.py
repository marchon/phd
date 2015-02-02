"""
The MIT License

Copyright (c) Jared Flatow 2014   http://www.flatown.com

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""



from math import exp
from numpy import array, ones, zeros

class Logistic(object):
    def __init__(self, theta):
        self.theta = theta

    def __call__(self, x):
        return 1. / (1. + exp(theta.dot(x)))

def logistic(z):
    return 1. / (1. + exp(-z))

def gl_regression(X, y, h=logistic, N=10000):
    theta = zeros(len(X[0]))
    for k in xrange(1, N):
        for i, x in enumerate(X):
            theta = array([theta[j] + (1. / k) * (y[i] - h(theta.dot(x))) * x_
                           for j, x_ in enumerate(x)])
    return theta
