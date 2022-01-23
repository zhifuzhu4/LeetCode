"""
3. Longest Substring Without Repeating Characters
Given a string s, find the length of the longest substring without repeating characters.

Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 10**4
s consists of English letters, digits, symbols and spaces.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        condition used[c] >= start is essential.
        e.g., s = "tmmzuxt", without the condition, the last 't' will be ignored since 't' appeared before.
        But in the string, the first 't' is before the 'start' variable, which is set to 2 for letter 'm'.
        so the 1st 't' should not be considered.
        the '=' of '>=' is essential too. e.g., s = "abcabcbb"
        """
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and used[c] > start:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length
