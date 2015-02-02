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





-module(combinator).

-export([factorial/1, x/1, y/1, z/1]).

%% the factorial step function
%% takes a function Self which is the result of fact(Self)
%% (i.e. Self =:= fact(Self))
%% the trick is that Self isn't evaluated until you need it
%% (see step #6 below)
%% when you call the thing returned by the combinator with an argument N
%% Self gets created with the ability to call itself if needed
%% at which point it winds up a stack of references to itself
%% it continues until it gets the argument 0
%% at which point it no longer needs to reference Self
%% so it can unwind, returning the initial value 1

fact(Self) ->
    fun (0) ->
            1;
        (N) ->
            N * Self(N - 1)
    end.

factorial(N) when is_integer(N) ->
    (z(fun fact/1))(N).

%% the classic Y combinator (with more meaningful variable names)

y(Step) ->
    %% n indicates control flow
    %% * indicates a function call
    %% ** an almost recursive call
    %% *** the true recursive call
    %%                                  Self
    %%    2        9*   4**  3           1    7        8*   6*** 5
    (fun (Self) -> Step(Self(Self)) end)(fun (Self) -> Step(Self(Self)) end).

%% the 'refactored' X and Z combinators

recur(X) ->
    X(X).

%% X is just a more compact Y

x(Step) ->
    recur(fun (Self) -> Step(Self(Self)) end).


%% Z is an applicative-order fixed-point combinator (e.g. for Erlang)
%% it wraps Self so that it can reference itself without calling the recursion

z(Step) ->
    recur(fun (Self) -> Step(fun (Y) -> (Self(Self))(Y) end) end).
