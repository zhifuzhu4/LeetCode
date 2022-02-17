"""
1304. Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]

Example 3:
Input: n = 1
Output: [0]

Constraints:
1 <= n <= 1000
"""

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        # Asymmetric List: (e.g. [1,2,3,4,5,-15])
        # Need to use range(1, n) instead of range(n-1), otherwise, it returns [0, 0] when n = 2
        # sum([]) -> 0
        return list(range(1, n)) + [-sum(range(1, n))]

    def sumZero2(self, n: int) -> List[int]:
        # Symmetric List: (e.g. [-2,-1,0,1,2] or [-3,-2,-1,1,2,3])
        # [0] * 0 -> []
        # n = 5, n // 2 -> 2, -(n // 2) -> -2, -n//2 = -3
        return list(range(-(n//2), 0)) + [0] * (n % 2) + list(range(1, n//2 + 1))

    def sumZero3(self, n: int) -> List[int]:
        res = []
        for i in range(1, n//2 + 1):
            res.append(i)
            res.append(-i)
        return res + [0] if n % 2 else res

