"""
367. Valid Perfect Square

Given a positive integer num, write a function which returns True if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.

Example 1:
Input: num = 16
Output: true

Example 2:
Input: num = 14
Output: false

Constraints:
1 <= num <= 2**31 - 1
"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # set left = 0 include all possible elements
        # set right = num + 1 to include corner cases, like n = 1
        left, right = 0, num+1
        while left < right:
            mid = left + (right - left) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 > num:
                right = mid
            else:
                left = mid + 1
        return False

    def isPerfectSquare2(self, num: int) -> bool:
        """ Newton's method
        https://en.wikipedia.org/wiki/Newton%27s_method
        this problem is to get the root of f(x) = num - x^2
        => x_next = x - f(x)/f'(x), for this problem f'(x) = -2x
        therefore, x_next = x - (num - x^2)/(-2x) = (x + num/x)/2
        """
        x = num
        while x**2 > num:
            x = (x + num/x) // 2
        return x**2 == num
