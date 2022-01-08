"""
461. Hamming Distance
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, return the Hamming distance between them.

Example 1:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.

Example 2:
Input: x = 3, y = 1
Output: 1

Constraints:
0 <= x, y <= 2**31 - 1
"""


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        1 ^ 4
          0001
        ^ 0100
        = 0101 -> two 1's
        :param x:
        :param y:
        :return:
        """
        return bin(x ^ y).count('1')

    def hammingDistance2(self, x: int, y: int) -> int:
        xor = x ^ y
        cnt = 0
        for _ in range(32):
            cnt += xor & 1
            xor = xor >> 1
        return cnt
