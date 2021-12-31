"""
509. Fibonacci Number

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

0, 1, 1, 2, 3, 5, ...

Constraints:
0 <= n <= 30
"""


class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n

        res = [0, 1]
        for i in range(2, n+1):
            res = [res[1], res[0] + res[1]]
        return res[1]

    def fib2(self, n: int) -> int:
        # math, https://en.wikipedia.org/wiki/Fibonacci_number
        golden_ratio = (1 + 5 ** 0.5) / 2
        res = (golden_ratio ** n - (1 - golden_ratio) ** n) / 5 ** 0.5
        return int(res)
