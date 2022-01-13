"""
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index.
If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 10**5
s consists of only lowercase English letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for x in s:
            d[x] = d.get(x, 0) + 1
        # s_ct = collections.Counter(s)

        for i, c in enumerate(s):
            if d[c] == 1:
                return i
        return -1
