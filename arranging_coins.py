"""
441. Arranging Coins

You have n coins and you want to build a staircase with these coins.
The staircase consists of k rows where the ith row has exactly i coins.
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:
1 <= n <= 2**31 - 1

Note:
sum of arithmetic progression is: (a1 + an)*n/2

roots of ax^2 + bx + c = 0
(-b +/- sqrt(b^2 - 4ac)/2a

(a1 + an)*n/2 <= n -> (1+x)*x/2 <= n -> x^2 + x - 2n <= 0
-> x = (-1 + sqrt(1 + 8n))/2
"""


class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((-1 + (8 * n + 1) ** 0.5)/2)

    def arrangeCoins2(self, n: int) -> int:
        left, right = 0, n + 1
        while left < right:
            mid = left + (right - left) // 2
            if (1+mid)*mid/2 > n:
                right = mid
            else:
                left = mid + 1
        return left - 1
