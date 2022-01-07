"""
190. Reverse Bits
Reverse bits of a given 32 bits unsigned integer.

Input: 43261596
Output: 964176192
Explanation:
43261596 represented in binary as 00000010100101000001111010011100,
return 964176192 represented in binary as 00111001011110000010100101000000.

TODO: study the bit solution
"""


class Solution:
    def reverseBits(self, n: int) -> int:
        # bin(8) -> '0b1010', '0b' means it's a binary number
        bins = bin(n)[2:][::-1]
        rev = bins + '0' * (32 - len(bins))
        return int(rev, 2)

    def reverseBits2(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans
