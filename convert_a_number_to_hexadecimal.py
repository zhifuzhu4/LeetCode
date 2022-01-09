"""
405. Convert a Number to Hexadecimal

Given an integer num, return a string representing its hexadecimal representation.
For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters,
and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

Example 1:
Input: num = 26
Output: "1a"

Example 2:
Input: num = -1
Output: "ffffffff"

Constraints:
-2**31 <= num <= 2**31 - 1

Note:
https://en.wikipedia.org/wiki/Two%27s_complement
The two's complement of an N-bit number is defined as its complement with respect to 2N;
the sum of a number and its two's complement is 2N.

Main idea is to flip the negative number to positive by using following code:
# num = num + 2**32
Things need to know
In two's complement:
zero is 000....0000 = 0
Most negative number is -2^(n-1)
Most positive number is 2^(n-1) -1
in this question: n = 32

Two's complement:
Step 1: Transforming 0 to 1 and 1 to 0
Step 2: plus 1

for example: (8-bits) '11111111' and num = -1
Step 1 can become: '11111111' + num = '11111111' - '1' = '11111110'
Step 2: '11111110' + '1' = '11111111'
actually '11111111' = 2 ** 8 -1
so we can simplify step 1 and step 2 to : 2 ** 8 - 1 + num +1 = 2 ** 8 + num
"""


class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return '0'
        if num < 0:
            num += 2 ** 32

        d = '0123456789abcdef'
        res = ''
        while num:
            digit = num % 16
            res += d[digit]
            num //= 16
        return res[::-1]
