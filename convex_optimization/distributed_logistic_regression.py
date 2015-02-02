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

from disco.core import Job, Params, RecordIter

class LogisticRegress(Job):
    def map_reader(fd, url, size, params):
        i = Task.id
        z = params.z
        y = params.y[i] + params.rho * (params.x[i] - z)
        for A, b in iter:
            x = ...
            yield str(i), (x, y)

    def reduce(iter, params):
        for n, (i, (x, y)) in enumerate(iter):
            zhat += x + y / float(params.rho)
            yield i, (x, y)
        oob.put('z', zhat / n)

if __name__ == '__main__':
    params = Params(rho=1., z=0)

    while True:
        job = LogisticRegress(params=params)
        results = job.wait()
        for i, (x, y) in RecordIter(job.wait()):
