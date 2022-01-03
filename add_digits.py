"""
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0

Constraints:
0 <= num <= 2**31 - 1

Follow up: Could you do it without any loop/recursion in O(1) runtime?

Note:
N=(a[0] * 1 + a[1] * 10 + ...a[n] * 10 ^n),and a[0]...a[n] are all between [0,9]
we set M = a[0] + a[1] + ..a[n]
and another truth is that:
1 % 9 = 1
10 % 9 = 1
100 % 9 = 1
so N % 9 = a[0] + a[1] + ..a[n]

means N % 9 = M
so N = M (% 9)
as 9 % 9 = 0,so we can make (n - 1) % 9 + 1 to help us solve the problem when n is 9.as N is 9, ( 9 - 1) % 9 + 1 = 9

also read the analysis from: https://blog.csdn.net/fuxuemingzhu/article/details/49161129
"""

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum(int(x) for x in str(num))
        return num

    def addDigits2(self, num: int) -> int:
        if num == 0:
            return 0
        return (num-1) % 9 + 1
