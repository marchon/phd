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



def gcd(m, n):
    if not m:
        return n
    return gcd(n % m, m)

def gcd_gen(gcd, A):
    mm, m = 0, gcd
    yield mm
    for a in A:
        yield m
        mm, m = m, a * m + mm

def gcd_cert(m, n):
    m_, n_, d = 0, 1, n
    while m % d or n % d:
        d = m_ * m + n_ * n
        yield m_, n_, d
        m_, n_ = n_ - n // m * m_, m_

def primes(N):
    primes = set()
    for n in xrange(2, N + 1):
        if all(n % p for p in primes):
            yield n
            primes.add(n)

def composites(N):
    primes = set()
    for n in xrange(2, N + 1):
        if all(n % p for p in primes):
            primes.add(n)
        else:
            yield n

def farey(N):
    if N == 1:
        yield 0, 1
        yield 1, 1
    else:
        Fn_ = tuple(farey(N - 1))
        for i, (m, n) in enumerate(Fn_[:-1]):
            m_, n_ = Fn_[i + 1]
            yield m, n
            if n + n_ == N:
                yield m + m_, N
        yield Fn_[-1]

def stern_brocot(directions):
    m, n, m_, n_  = 0, 1, 1, 0
    for char in directions:
        if char.upper() == 'L':
            n_, m_ = n + n_, m + m_
        elif char.upper() == 'R':
            n, m = n + n_, m + m_
    return m + m_, n + n_

def brocot_stern(m, n):
    while m != n:
        if m < n:
            yield 'L'
            n = n - m
        else:
            yield 'R'
            m = m - n
