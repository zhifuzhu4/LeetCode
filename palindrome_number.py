"""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.
For example, 121 is palindrome while 123 is not.

Example 1:
Input: x = 121
Output: true

Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Example 4:
Input: x = -101
Output: false

Constraints:
-231 <= x <= 231 - 1

Follow up: Could you solve it without converting the integer to a string?

Note: single digit numbers (0-9) and letters (a-z, A-Z) are palindomes
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # the above two lines just to make the function more efficient.
        # Not essential since it's covered by the code below
        return str(x) == str(x)[::-1]


class Solution2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rst = 0
        while x > rst:
            rst = rst * 10 + x % 10
            x = x // 10
            print(f'x={x}, rst={rst}')
        return x == rst or x == rst // 10