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




def strval(string):
    return sum(ord(c) * 10**-n for n, c in enumerate(string.lower()))

from itertools import izip
from cvxopt import spmatrix

class Indicator(dict):
    def __init__(self, inverted):
        """
        for key, ids in inverted:
          self[key] = (n, ids)
        """
        super(Indicator, self).__init__((key, (n, ids))
                                        for n, (key, ids) in enumerate(inverted))

    @property
    def matrix(self):
        """
           _          -
        i | 0 | 1  ... |
          |  ...       |
          |_          _|
              j

        feature `i` exists in record `j`
        """
        return spmatrix(1, *izip(*((n, id)
                                   for n, ids in self.itervalues()
                                   for id in ids)))

class Numeric(Indicator):
    @property
    def matrix(self):
        """
           _          -
        i |  val   ... |
          |  ...       |
          |_          _|
              j

        feature `i` takes on value `val` in record `j`
        """
        return spmatrix(*izip(*((val, n, id)
                                for (feature, val), (n, ids) in self.iteritems()
                                for id in ids)))
