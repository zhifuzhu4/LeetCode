"""
191. Number of 1 Bits
Write a function that takes an unsigned integer and returns the number of '1' bits
it has (also known as the Hamming weight).

Example 1:
Input: n = 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

Example 2:
Input: n = 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.

Example 3:
Input: n = 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

Constraints:
The input must be a binary string of length 32.

Follow up: If this function is called many times, how would you optimize it?
"""


class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')

    def hammingWeight2(self, n: int) -> int:
        """ Using bit operation to cancel a 1 in each round
        Think of a number in binary n = XXXXXX1000, n - 1 is XXXXXX0111.
        n & (n - 1) will be XXXXXX0000 which is just remove the last significant 1
        e.g., bin(10) = '0b1010', bin(9) = '0b1001', 10 & 9 =>
           1010
         & 1001
         = 1000
         so it cancels the last 1 of '0b1010'. Next, 8 & 7
           1000
        &  0111
        =  0000
        """
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res
