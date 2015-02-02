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
Another approach to dynamic programming.

The example from `http://www.stanford.edu/class/ee365/lectures/det_sys`

>>> inf = float('inf')
>>> nodes = list('abcd')
>>> edges = {'ab': 2, 'ac': 6, 'bc': 3, 'bd': 8, 'cb': 1, 'cd': 4, 'dd': 0}
>>> step = lambda t, x, u, T: u
>>> cost = lambda t, x, u, T: edges.get(x + u, inf) if t < T - 1 else (0 if x == 'd' else inf)
>>> p = dict(policy(T=4, X=lambda t: nodes, U=lambda t, x: nodes, f=step, g=cost))
>>> P = {0: {'a': (9, 'b'), 'b': (7, 'c'), 'c': (4, 'd'), 'd': (0, 'd')}, \
         1: {'a': (10, 'b'), 'b': (7, 'c'), 'c': (4, 'd'), 'd': (0, 'd')}, \
         2: {'a': (inf, 'a'), 'b': (8, 'd'), 'c': (4, 'd'), 'd': (0, 'd')}, \
         3: {'a': (inf, 'a'), 'b': (inf, 'a'), 'c': (inf, 'a'), 'd': (0, 'a')}}
>>> p == P
True
"""

def step(t, x, u, T=None):
    """Return the state at time t + 1."""

def cost(t, x, u, T=None):
    """Return a real or infinite value."""

def policy(T, X, U, f=step, g=cost, p={}):
    V = lambda x: p.get(x, (0, None))[0]
    for t in reversed(xrange(T)):
        p = dict((x, min((g(t, x, u, T) + V(f(t, x, u, T)), u) for u in U(t, x))) for x in X(t))
        yield t, p
