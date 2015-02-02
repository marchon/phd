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



def hanoi(n):
    return 2 ** n - 1

def hanoi_r(n):
    if n == 0:
        return 0
    return 2 * hanoi_r(n - 1) + 1

def josephus(n):
    return ((n << 1) & ((1 << n.bit_length()) - 1)) + 1

def josephus_r(n):
    if n <= 1:
        return 1
    return 2 * josephus_r(n / 2) + (n % 2 or -1)

def f(n, alpha=1, beta=-1, gamma=1):
    if n <= 1:
        return alpha
    return 2 * f(n / 2) + (gamma if n % 2 else beta)
