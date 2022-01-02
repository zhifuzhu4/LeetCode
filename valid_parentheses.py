"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([)]"
Output: false

Example 5:
Input: s = "{[]}"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def validParentheses(self, s: str) -> bool:
        # Time Limit Exceeded
        # Replace function will replace only one set {} at a time.
        # Replace itself takes O(N) time because it will have to search the entire string.
        # On top of this, we have while loop which runs for O(N/2) times.
        # So O(N) * O(N/2) results in O(N^2)
        if len(s) % 2:
            return False

        while "()" in s or "[]" in s or "{}" in s:
            s = s.replace("()", "").replace("[]", "").replace("{}", "")
        return s == ""

    def validParentheses2(self, s: str) -> bool:
        # 1. if it's the left bracket then we append it to the stack
        # 2. else if it's the right bracket and the stack is empty(meaning no matching left bracket),
        # or the left bracket doesn't match
        # 3. finally check if the stack still contains unmatched left bracket
        stack = []
        d = {'(': ')', '[': ']', '{': '}'}
        for x in s:
            if x in d:  # 1
                stack.append(x)
            elif len(stack) == 0 or d[stack.pop()] != x:  # 2
                return False
        return len(stack) == 0  # 3, or stack == []
