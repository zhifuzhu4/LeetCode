"""
1446. Consecutive Characters

The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.

Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

Note:
1. Increase the counter by 1 if the next char same as the current one; otherwise, reset the counter to 1;
2. Update the max value of the counter during each iteration.
"""

import itertools


class Solution:
    def maxPower(self, s: str) -> int:
        ans = cnt = 1
        for i in range(len(s)-1):
            if s[i+1] == s[i]:
                cnt += 1
                ans = max(ans, cnt)
            else:
                cnt = 1
        return ans

    def maxPower2(self, s: str) -> int:
        return max(len(list(b)) for a, b in itertools.groupby(s))
