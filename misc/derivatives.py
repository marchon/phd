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



def args(f):
    return f.__code__.co_varnames

def nargs(f):
    return f.__code__.co_argcount

class limit(object):
    """
    As the input to `f` comes arbitrarily close to `c`,
    the output of `f` becomes arbitrarily close to this.
    """
    def __init__(self, f, c):
        self.f = f
        self.c = c

class derivative(object):
    """
    A measure of the change in the output of a function w.r.t. its input.
    """
    def __init__(self, f):
        self.f = f

class partial(derivative):
    """
    A measure of the change in the output of a function w.r.t. one of its inputs,
    while holding the others constant.
    """
    def __init__(self, f, i):
        super(partial, self).__init__(f)
        self.i = i

    def __call__(self, *args):
        return limit(lambda h: (self.f(*[arg + h if i == self.i else arg
                                         for i, arg in enumerate(args)]) -
                                self.f(*args)) / h, 0)

    @property
    def __code__(self):
        return self.f.__code__

    @property
    def __name__(self):
        return '\u2202%s/\u2202%s' % (self.f.__name__, args(self.f)[self.i])

    def __repr__(self):
        return self.__name__

def gradient(y):
    return [partial(y, i) for i in range(nargs(y))]

def hessian(y):
    return jacobian(gradient(y))

def jacobian(Y):
    return [gradient(y) for y in Y]
