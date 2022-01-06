"""
326. Power of Three

Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3**x.

Example 1:
Input: n = 27
Output: true

Example 2:
Input: n = 0
Output: false

Example 3:
Input: n = 9
Output: true

Constraints:
-2**31 <= n <= 2**31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n = n // 3
        return n == 1

    def isPowerOfThree2(self, n: int) -> bool:
        # 3**20 > 2**31
        return n > 0 and 3 ** 20 % n == 0

    def isPowerOfThree3(self, n: int) -> bool:
        nums = [3**x for x in range(21)]
        return n in nums
