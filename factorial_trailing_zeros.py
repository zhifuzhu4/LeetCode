"""
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.
Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.

Example 1:
Input: n = 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: n = 5
Output: 1
Explanation: 5! = 120, one trailing zero.

Example 3:
Input: n = 0
Output: 0

Constraints:
0 <= n <= 10**4

Follow up: Could you write a solution that works in logarithmic time complexity?

Note:
计算包含的2和5组成的pair的个数就可以了。
因为5的个数比2少，所以2和5组成的pair的个数由5的个数决定。
观察15! = 有3个5(来自其中的5, 10, 15)， 所以计算n/5就可以。
但是25! = 有6个5(有5个5来自其中的5, 10, 15, 20, 25， 另外还有1个5来自25=(5*5)的另外一个5），
所以除了计算n/5， 还要计算n/5/5, n/5/5/5, n/5/5/5/5, …, n/5/5/5,/5直到商为0。
"""


class Solution:
    def trailingZeros(self, n: int) -> int:
        res = 0
        while n > 0:
            n = n // 5
            res += n
        return res
