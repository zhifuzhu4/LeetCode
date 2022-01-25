"""
693. Binary Number with Alternating Bits
Given a positive integer, check whether it has alternating bits: namely,
if two adjacent bits will always have different values.

Example 1:
Input: n = 5
Output: true
Explanation: The binary representation of 5 is: 101

Example 2:
Input: n = 7
Output: false
Explanation: The binary representation of 7 is: 111.

Example 3:
Input: n = 11
Output: false
Explanation: The binary representation of 11 is: 1011.

Constraints:
1 <= n <= 2**31 - 1
"""


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return '00' not in bin(n) and '11' not in bin(n)

    def hasAlternatingBits2(self, n: int) -> bool:
        while n:
            res1 = n & 1
            n >>= 1
            res2 = n & 1
            if res1 == res2:
                return False
        return True

    def hasAlternatingBits3(self, n: int) -> bool:
        while n:
            if not 0 < (n & 3) < 3:
                return False
            n >>= 1  # n >>= 2 doesn't work, e.g., n = 6
        return True
