"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Note:
An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once. e.g., listen -> silent, cinema -> iceman

The all() function returns True if all items in an iterable are true, otherwise it returns False.
If the iterable object is empty, the all() function also returns True.
all([True, True, True]) -> True
all([True, True, False]) -> False
all([]) -> True
"""
import string
from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def isAnagram2(self, s: str, t: str) -> bool:
        return Counter(t) == Counter(s)

    def isAnagram3(self, s: str, t: str) -> bool:
        return all([s.count(c) == t.count(c) for c in string.ascii_lowercase])
