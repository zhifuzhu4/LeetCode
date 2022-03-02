"""
392. Is Subsequence
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some
(can be none) of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false

Constraints:
0 <= s.length <= 100
0 <= t.length <= 10**4
s and t consist only of lowercase English letters.

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109,
and you want to check one by one to see if t has its subsequence.
In this scenario, how would you change your code?

TODO: study solution for follow-up
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        Complexity
        Time: O(M + N), where M <= 100 is length of s string, N <= 10^4 is length of t string.
        Space: O(1)
        """
        i = 0
        for c in t:
            if i == len(s):  # If match full s -> then s is a subsequence
                return True
            if s[i] == c:
                i += 1
        return i == len(s)

    def isSubsequence2(self, s: str, t: str) -> bool:
        # two pointers
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)

    def isSubsequence3(self, s: str, t: str) -> bool:
        # str.find(sub, start, end)
        # Returns the lowest index of the substring if it is found, otherwise, returns -1.
        start = 0
        for c in s:
            ind = t.find(c, start)
            if ind == -1:
                return False
            start = ind + 1
        return True

    def isSubsequence4(self, s: str, t: str) -> bool:
        """
        str.index(str, beg=0 end=len(string))
        Returns the first position of the substring found. Otherwise, raise an exception.
        """
        for c in s:
            try:
                ind = t.index(c)
            except ValueError:
                return False
            t = t[ind+1:]
        return True
