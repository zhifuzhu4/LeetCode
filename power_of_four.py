"""
342. Power of Four
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4**x.

Example 1:
Input: n = 16
Output: true

Example 2:
Input: n = 5
Output: false

Example 3:
Input: n = 1
Output: true

Constraints:
-2**31 <= n <= 2**31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 4 == 0:
            n = n // 4
        return n == 1

    def isPowerOfFour2(self, n: int) -> bool:
        nums = [4**x for x in range(16)]
        return n in nums

    def isPowerOfFour3(self, n: int) -> bool:
        """
        Every power of 2:
        0000 0001 = 1
        0000 0100 = 4
        0001 0000 = 16
        0100 0000 = 64
        ...
        we can see that number 1 is always located at odd position.
        So we can use the bitwise AND operator & between n and
           1010101010101010101010101010101 (the biggest 32 bit number with 1 at all odd positions)
         & 0000000000000000000000000000001
         = 0000000000000000000000000000001 (only the 1 at the odd position results in 1, all others are 0s)
        int('1010101010101010101010101010101', 2) -> 1431655765
        """
        return n > 0 and n & (n-1) == 0 and n & 1431655765 == n
