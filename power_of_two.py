"""
231. Power of Two

Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2**x.

Example 1:
Input: n = 1
Output: true
Explanation: 2**0 = 1

Example 2:
Input: n = 16
Output: true
Explanation: 2**4 = 16

Example 3:
Input: n = 3
Output: false

Constraints:
-2**31 <= n <= 2**31 - 1

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            while n % 2 == 0:
                n = n // 2
            return n == 1

    def isPowerOfTwo2(self, n: int) -> bool:
        return n > 0 and 2**31 % n == 0

    def isPowerOfTwo3(self, n: int) -> bool:
        nums = [2**x for x in range(32)]
        return n in nums

    def isPowerOfThree4(self, n: int) -> bool:
        """ bin() returns the binary string of a given integer
        bin(2) -> '0b10' bin(4) -> '0b100', bin(8) -> '0b1000' ...
        '0b' means it is a base 2 number/binary number
        https://en.wikipedia.org/wiki/Binary_number#Representation """
        if n < 1:
            return False
            # above two lines are necessary since bin(-2) -> '-0b10'
        else:
            return bin(n).count('1') == 1

    def isPowerOfThree5(self, n: int) -> bool:
        """ & is the bitwise AND operator, https://www.geeksforgeeks.org/python-bitwise-operators/
            16 & 15 ->
            10000
              &
            01111
          = 00000
          = 0 (decimal)
        """
        return n > 0 and n & (n-1) == 0
