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
Bellman equations for random variables (Markov Decision Problems)

Examples from: http://www.stanford.edu/class/ee365/lectures/dp.pdf

Our old friend, inventory:

>>> inf = float('inf')
>>> T = 50
>>> C = 6
>>> X = lambda t: range(C + 1)
>>> mdp = MDP(T, X, W=lambda t, x, u: {0: .7, 1: .2, 2: .1})
>>> mdp.step = lambda t, x, u, d: x - d + u
>>> mdp.cost = lambda t, x, u, d: .1 * x + 1 * (u > 0) if 0 <= x - d + u <= C else inf
>>> mu = dict(mdp.policy())
>>> [t for t, p in mu.items() if [u for x, (v, u) in p.items()] == [4, 3, 0, 0, 0, 0, 0]] == range(T - 2)
True
"""

class MDP(object):
    def __init__(self, T, X, U=None, W=None):
        self.T = T
        self.X = X
        self.U = U or (lambda t, x: X(t))
        self.W = W or (lambda t, x, u: {None: 1})

    def step(self, t, x, u, w):
        """Return the state at time t + 1."""

    def cost(self, t, x, u, w):
        """Return a real or infinite stage cost."""

    def policy(self, p={}):
        f = self.step
        g = self.cost
        E = lambda t, x, u, W: sum((g(t, x, u, w) + V(t, f(t, x, u, w))) * p for w, p in W.items())
        V = lambda t, x: p.get(x, (0, None))[0]
        for t in reversed(xrange(self.T)):
            p = dict((x, min((E(t, x, u, self.W(t, x, u)), u) for u in self.U(t, x))) for x in self.X(t))
            yield t, p
