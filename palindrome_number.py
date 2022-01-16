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
-2**31 <= x <= 2**31 - 1

Follow up: Could you solve it without converting the integer to a string?

Note: single digit numbers (0-9) and letters (a-z, A-Z) are palindomes
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        # the above two lines just to make the function more efficient.
        # Not essential since it's covered by the code below

        # [::-1] works for: string, list, and tuple
        # e.g., 'abc'[::-1] -> 'cba',
        # [1, 2, 3][::-1] -> [3, 2, 1]
        # (1, 2, 3)[::-1] -> (3, 2, 1)
        return str(x) == str(x)[::-1]

    def isPalindrome2(self, x: int) -> bool:
        # reverse the number first and see if it is equal to the original number
        if x < 0:
            return False
        orig_x = x
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10
        return rev == orig_x

    def isPalindrome3(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        i, j = 0, len(x)-1
        while i < j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
            # it's easy to foget the above two lines that causes TLE (Time Limit Exceeded)
        return True
