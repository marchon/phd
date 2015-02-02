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
Trading example from: http://www.stanford.edu/class/ee365/lectures/trading.pdf
"""
import math
import decision

inf = float('inf')
cut = lambda v, m, M: min(max(v, m), M)

class Trader(decision.MDP):
    def __init__(self, T=250, qmin=-5, qmax=15, gamma=.005, N=20):
        def transition(n):
            l = 2 * math.log(prices[n])
            a = cut(.4 - l, .01, .98)
            b = cut(.4 + l, .01, .98)
            return {n + 1: a, n - 1: b, n: 1 - a - b}
        prices = self.prices = dict((n, (1 + gamma) ** n) for n in range(-N, N + 1))
        ptrans = self.ptrans = dict((n, transition(n)) for n in range(-N, N + 1))
        states = [(q, n) for q in range(qmin, qmax + 1) for n in range(-N, N + 1)]
        self.T = T
        self.X = lambda t: states
        self.U = lambda t, (q, n): range(qmin - q, qmax - q + 1)
        self.W = lambda t, (q, n), u: ptrans[n]

    def step(self, t, (q, n), u, n_):
        return q + u, n_

    def cost(self, t, (q, n), u, n_):
        if t < self.T - 1:
            return u * self.prices[n]
        return 0 if q + u == 0 else inf

class TraderSH(Trader):
    def cost(self, t, (q, n), u, n_):
        if t < self.T - 1:
            return u * self.prices[n] + (.005 if q < 0 else 0)
        return 0 if q + u == 0 else inf

class TraderLin(Trader):
    def cost(self, t, (q, n), u, n_):
        if t < self.T - 1:
            return u * self.prices[n] + (.005 * abs(u))
        return 0 if q + u == 0 else inf

class TraderSHNL(Trader):
    def cost(self, t, (q, n), u, n_):
        if t < self.T - 1:
            return u * self.prices[n] + (.0001 if q < 0 else 0) + (.005 * abs(u) ** 1.5)
        return 0 if q + u == 0 else inf

def plot(policy, T=0):
    import mpl_toolkits.mplot3d
    import pylab
    o = policy[T]
    f = pylab.figure()
    a = f.add_subplot(111, projection='3d')
    a.plot_trisurf([q for q, _ in o], [p for _, p in o], [u for v, u in o.values()], cmap=pylab.cm.jet)
    a.set_xlabel('Quantity')
    a.set_ylabel('Price')
    a.set_zlabel('Action')
    pylab.show()

if __name__ == '__main__':
    for trader in (Trader, TraderSH, TraderLin, TraderSHNL):
        plot(dict(trader(T=25).policy()))
