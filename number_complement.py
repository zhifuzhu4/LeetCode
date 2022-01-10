"""
476. Number Complement
The complement of an integer is the integer you get when you flip all the 0's to 1's
and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary
and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

Example 1:
Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits),
and its complement is 010. So you need to output 2.

Example 2:
Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits),
and its complement is 0. So you need to output 0.

Constraints:

1 <= num < 2**31
"""


class Solution:
    def findComplement(self, num: int) -> int:
        bins = bin(num)[2:]
        res = ''
        for x in bins:
            if x == '0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)

    def findComplement2(self, num: int) -> int:
        """
        map(fun, iter)
        fun : It is a function to which map passes each element of given iterable.
        iter : It is a iterable which is to be mapped.
        """
        bins = bin(num)[2:]
        res = map(lambda x: '1' if x == '0' else '0', bins)
        return int(''.join(res), 2)

    def findComplement3(self, num: int) -> int:
        """ e.g., 5 = 101, and its complement is 010 = 2
        101 ^ 111 = 010, xor with 111 will flip all the 0's to 1's
        we just need to find out the number with all 1's that has the same length of num
        """
        n = len(bin(num)[2:]) * '1'
        return num ^ int(n, 2)

    def findComplement4(self, num: int) -> int:
        """ the above solution uses bin() to get the length of num,
        this solution finds the length without using bin()
        left shift works as multiplication by power of 2 and it finds the 1st number bigger than num,
        e.g., 1st number bigger than num = 5 is 2**3 = 8, -> 1000, and 7 (8-1) -> 111 has the sane length of 5 (101)
        """
        n = 1
        while n <= num:
            n <<= 1
        return (n - 1) ^ num
