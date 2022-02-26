"""
1281. Subtract the Product and Sum of Digits of an Integer
Given an integer number n, return the difference between the product of its digits and the sum of its digits.

Example 1:
Input: n = 234
Output: 15
Explanation:
Product of digits = 2 * 3 * 4 = 24
Sum of digits = 2 + 3 + 4 = 9
Result = 24 - 9 = 15

Example 2:
Input: n = 4421
Output: 21
Explanation:
Product of digits = 4 * 4 * 2 * 1 = 32
Sum of digits = 4 + 4 + 2 + 1 = 11
Result = 32 - 11 = 21

Constraints:
1 <= n <= 10^5
"""


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_, prod = 0, 1
        while n:
            prod *= n % 10
            sum_ += n % 10
            n //= 10
        return prod - sum_

    def subtractProductAndSum2(self, n: int) -> int:
        # eval('*'.join('abcd')) -> 'a*b*c*d'
        return eval('*'.join(str(n))) - eval('+'.join(str(n)))
