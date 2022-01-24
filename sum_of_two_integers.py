"""
371. Sum of Two Integers
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1:
Input: a = 1, b = 2
Output: 3

Example 2:
Input: a = 2, b = 3
Output: 5

Constraints:
-1000 <= a, b <= 1000
"""


class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        https://leetcode.com/problems/sum-of-two-integers/discuss/489210/Read-this-if-you-want-to-learn-about-masks
        """
        # 32 bit mask in hexadecimal
        mask = 0xffffffff

        # works both as while loop and single value check
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        # handles overflow
        return (a & mask) if b > 0 else a

