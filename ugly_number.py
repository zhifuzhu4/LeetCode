"""
263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.

Example 1:
Input: n = 6
Output: true
Explanation: 6 = 2 × 3

Example 2:
Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.

Example 3:
Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

Constraints:
-2**31 <= n <= 2**31 - 1

Note:
To eliminate factors 2,3,5 from given number n. If anything left after eliminating these is > 1,
then the number is not ugly else it is.

10 = 5*2, 8 = 2^3, 6 = 2*3. Basically, all these numbers are multiples of 2, 3, 5
and they will save on additional loops since they are in the descending order.

For example, if num = 80, num will reduce like this 80 -> 8 -> 1 since you start with x = 10
and then x = 8. So, this just takes two steps. If you just used [2, 3, 5] for num = 80
it will take num 5 steps like this 80 -> 40 -> 20 -> 10 -> 5 -> 1.
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        for x in [10, 8, 6, 5, 3, 2]:
            while n % x == 0:
                n = n // x
        return n == 1

    def isUgly2(self, n: int) -> bool:
        if n <= 0:
            return False
        elif n == 1:
            return True
        else:
            return (2 * 3 * 5) ** 31 % n == 0
