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




class Allocator(object):
    def __init__(self, a, b, g, h):
        self.a, self.b = a, b
        self.g, self.h = g, h

    def xs(self, x, *ys):
        yield x
        for y in ys:
            x = self.a * y + self.b * (x - y)
            yield x

    def R(self, x, *ys):
        return sum(self.g(yi) + self.h(xi - yi)
                   for xi, yi in zip(self.xs(x, *ys), ys))

    def f(self, N=0):
        """
        maximize over integer values of 0 <= y <= x
        """
        def payoff(x, y):
            p, _y = self.f(N - 1)(self.a * y + self.b * (x - y)) if N else (0, 0)
            return self.g(y) + self.h(x - y) + p
        return lambda x: max((payoff(x, y), y) for y in xrange(int(x + 1)))
