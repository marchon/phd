""" 
LICENSE TYPE: MIT

Received: from [192.168.2.2] (adsl-76-254-50-95.dsl.pltn13.sbcglobal.net [76.254.50.95])
	(Authenticated sender: jared@skej.us)
	by relay6-d.mail.gandi.net (Postfix) with ESMTPSA id D9F06FB883
	for <marchon@gmail.com>; Sun,  2 Nov 2014 08:05:18 +0100 (CET)
From: Jared Flatow <jflatow@gmail.com>
Content-Type: multipart/alternative; boundary="Apple-Mail=_A174274C-E60A-4BEC-B9E6-8EAACA36F10A"
Message-Id: <7AC2783C-4844-4C47-B724-47E6C8DEE4F9@gmail.com>
Mime-Version: 1.0 (Mac OS X Mail 6.6 \(1510\))
Subject: Re: I just cloned your github library phd.git
Date: Sun, 2 Nov 2014 00:05:15 -0700
References: <CAC938DiY8u2iVk2ByKRBJYY1aGbEavqsBVUnewGZvh1HfJTSCQ@mail.gmail.com>
To: George Lambert <marchon@gmail.com>
In-Reply-To: <CAC938DiY8u2iVk2ByKRBJYY1aGbEavqsBVUnewGZvh1HfJTSCQ@mail.gmail.com>
X-Mailer: Apple Mail (2.1510)


--Apple-Mail=_A174274C-E60A-4BEC-B9E6-8EAACA36F10A
Content-Transfer-Encoding: quoted-printable
Content-Type: text/plain;
	charset=windows-1252

Yes I hereby grant you such a license :) Thanks for asking first.

I look forward to seeing what you do with it! I never used it for =
anything practical. I should probably continue with the extending to =
higher dimensions at some point, Dr. Wildberger confirmed that I was =
going in the right direction=85

best,
jared

""" 
_License = 'MIT'  

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


"""
Some rational universal hyperbolic geometry as per the inimitable Norman J. Wildberger.

Much of this code would be unnecessary to do practical calculations.
We include a smattering of linear algebra so that the module can be self-contained.
And the symmetries between points and lines are made explicit for educational purposes.
Formulas are also written according to their definitions instead of using shortcuts.

Most of this implementation should generalize to higher dimensions, whatever that means.
"""
from fractions import Fraction
from collections import namedtuple, Sequence

def cofactor(A, i=0, j=0):
    return (-1 if (i + j) % 2 else 1) * minor(A, i, j)

def cofactors(A, i=0):
    return [cofactor(A, j=j) for j in xrange(len(A))]

def determinant(A, j=0):
    if len(A) == 1:
        return A[0][0]
    return sum(A[i][j] * cofactor(A, i, j) for i in xrange(len(A)))

def minor(A, i=0, j=0):
    return determinant([row[:j] + row[j + 1:] for row in A[:i] + A[i + 1:]])

def trace(A):
    return sum(A[i][i] for i in xrange(len(A)))

def ratio(X, Y):
    for x, y in zip(X, Y):
        return Fraction(x, y)

def dot(X, Y):
    return sum(x * y for x, y in zip(X, Y))

def add(X, Y):
    return [x + y for x, y in zip(X, Y)]

def sub(X, Y):
    return [x - y for x, y in zip(X, Y)]

def mul(X, a):
    return [x * a for x in X]

def div(X, a):
    return [x / a for x in X]

def isseq(seq):
    return isinstance(seq, Sequence)

def partitions(seq):
    for i, x in enumerate(seq):
        yield x, seq[:i] + seq[i + 1:]

def signed(seq): # XXX: correct this for N-dimensional hyperbolic space
    X = list(seq)
    return X and X[:-1] + [-X[-1]]

def cross_ratio(a, b, c, d):
    return Fraction(ratio(a & c, b & c), ratio(a & d, b & d))

def quadrance(a1, a2):
    return cross_ratio(a1, a2.conjugate(a1), a2, a1.conjugate(a2))

def spread(A1, A2):
    return cross_ratio(A1, A2.conjugate(A1), A2, A1.conjugate(A2))

def join(*points):
    return line(*signed(cofactors(([], ) + points)))

def meet(*lines):
    return point(*signed(cofactors(([], ) + lines)))

def null(t, u):
    return u * u - t * t, 2 * u * t, u * u + t * t

def side(a, b):
    return a, b

def vertex(A, B):
    return A, B

def couple(a, L):
    return a, L

def incident(a, L):
    return sum(signed(ai * Li for ai, Li in zip(a, L))) == 0

class matrix(tuple):
    def __new__(cls, *args):
        return super(matrix, cls).__new__(cls, args)

    def __repr__(self):
        return self.__class__.__name__ + super(matrix, self).__repr__()

    def __neg__(self):
        if isseq(self[0]):
            return type(self)(*(mul(v, -1) for v in self))
        return type(self)(*mul(self, -1))

    def __add__(self, o):
        if isseq(self[0]):
            return matrix(*(add(v, x) for v, x in zip(self, o)))
        return vector(*add(self, o))

    def __sub__(self, o):
        if isseq(self[0]):
            return matrix(*(sub(v, x) for v, x in zip(self, o)))
        return vector(*sub(self, o))

    def __mul__(self, o):
        if isseq(o):
            if isseq(o[0]):
                return matrix(*zip(*([dot(row, x) for row in self] for x in zip(*o))))
            if isseq(self[0]):
                return vector(*(dot(row, o) for row in self))
            return dot(self, o)
        if isseq(self[0]):
            return type(self)(*(mul(v, o) for v in self))
        return type(self)(*mul(self, o))

    def __div__(self, o):
        if isseq(self[0]):
            return type(self)(*(div(v, o) for v in self))
        return type(self)(*div(self, o))

    def __xor__(self, o):
        return self * o - matrix(*o) * self

    def det(self):
        return determinant(self)

    def tr(self):
        return trace(self)

class vector(matrix):
    def __pow__(self, o):
        return matrix(*(mul(v, o) for v in self))

    def projective((x, y, z)): # XXX: generalize to N dims
        return matrix([y, x + y], [x - y, -y])

    @classmethod
    def null(cls, t, u):
        return cls(*null(t, u))

class point(vector):
    def __and__(self, a):
        return join(self, a)

    def conjugate(self, a):
        return self & a & self.dual()

    def altitude(self, L):
        return self & L.dual()

    def parallel(self, L):
        return self & L.altitude(self)

    def base(self, L):
        return L.altitude(self) & L.dual()

    def isdual(self, L):
        return concurrent(self.dual(), L)

    def isperpendicular(self, other):
        return incident(other, self.dual())

    def dual(self):
        return line(*self)

    def polar(self):
        return self.dual()

class line(vector):
    def __and__(self, L):
        return meet(self, L)

    def conjugate(self, L):
        return self & (self & L).dual()

    def altitude(self, a):
        return a.dual() & self

    def parallel(self, a):
        return a.dual() & a.altitude(self)

    def base(self, a):
        return a.altitude(self) & self

    def isdual(self, a):
        return concurrent(a.dual(), self)

    def isperpendicular(self, other):
        return incident(self.dual(), other)

    def dual(self):
        return point(*self)

    def pole(self):
        return self.dual()

class triangle(namedtuple('triangle', ('a1', 'a2', 'a3'))):
    def __new__(cls, *points):
        return super(triangle, cls).__new__(cls, *(point(*p) for p in points))

    def associate(self):
        return trilateral(*(meet(*y) for _, y in partitions(self)))

    def altitudes(self):
        for x, y in partitions(self):
            yield x.altitude(meet(*y))

    def orthocenter(self):
        N1, N2, _ = self.altitudes()
        return N1 & N2

    def orthic(self):
        return triangle(*(N & L for N, L in zip(self.altitudes(), self.associate())))

    def isdual(self):
        return any(x.isdual(join(*y)) for x, y in partitions(self))

class trilateral(namedtuple('trilateral', ('L1', 'L2', 'L3'))):
    def __new__(cls, *lines):
        return super(trilateral, cls).__new__(cls, *(line(*l) for l in lines))

    def associate(self):
        return triangle(*(meet(*Y) for _, Y in partitions(self)))

    def altitudes(self):
        for X, Y in partitions(self):
            yield X.altitude(join(*Y))

    def ortholine(self):
        n1, n2, _ = self.altitudes()
        return n1 & n2

    def isdual(self):
        return any(isdual(meet(*Y), X) for X, Y in partitions(self))
