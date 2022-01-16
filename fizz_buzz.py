"""
412. Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

Example 1:
Input: n = 3
Output: ["1","2","Fizz"]

Example 2:
Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]

Example 3:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

Constraints:
1 <= n <= 10**4
"""

from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = list(range(1, n+1))
        for i, x in enumerate(res):
            if x % 3 == 0 and x % 5 == 0:
                res[i] = 'FizzBuzz'
            elif x % 3 == 0:
                res[i] = 'Fizz'
            elif x % 5 == 0:
                res[i] = 'Buzz'
        return [str(x) for x in res]

    def fizzBuzz2(self, n: int) -> List[str]:
        res = []
        base3, base5, base15 = 3, 5, 15
        for i in range(1, n+1):
            if i == base15:
                res.append('FizzBuzz')
                base3 = base15 + 3
                base5 = base5 + 5
                base15 += 15
            elif i == base3:
                res.append('Fizz')
                base3 += 3
            elif i == base5:
                res.append('Buzz')
                base5 += 5
            else:
                res.append(str(i))
        return res