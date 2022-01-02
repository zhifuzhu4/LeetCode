"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:
1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.

Note: use of min/max
If the values are strings, the string with the lowest value in alphabetical order is returned.
min('abcd', 'b') -> 'abcd'
min(['abcd', 'b']) -> 'abcd'

min(['abcd', 'b'], key=len) -> 'b'
"""

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lowest = min(strs)
        highest = max(strs)

        for i, ch in enumerate(lowest):
            if ch != highest[i]:
                return lowest[:i]
        return lowest
