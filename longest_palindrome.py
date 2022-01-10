"""
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters,
return the length of the longest palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1

Example 3:
Input: s = "bb"
Output: 2

Constraints:
1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
"""

import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        num_odds = sum([1 & x for x in collections.Counter(s).values()])
        return len(s) - num_odds + bool(num_odds)

    def longestPalindrome2(self, s: str) -> int:
        odds = set()
        for c in s:
            if c not in odds:
                odds.add(c)
            else:
                odds.remove(c)
        # len(odds) is the number of odd letters
        return len(s) - len(odds) + 1 if len(odds) > 0 else len(s)
