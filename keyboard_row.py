"""
500. Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet
on only one row of American keyboard like the image below.

In the American keyboard:
the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:
Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]

Example 2:
Input: words = ["omk"]
Output: []

Example 3:
Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

Constraints:
1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase).
"""

from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        set operators
        s1.issubset(s2) <=> s1 <= s2
        s1.issuperset(s2) <=> s1 >= s2
        s1.isdisjoint(s2), no corresponding operator
        a = {1, 2}
        b = {1, 2, 3}
        a <= b -> True
        b >= a -> True
        """
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for word in words:
            w = set(word.lower())
            if w <= row1 or w <= row2 or w <= row3:
                res.append(word)
        return res

    def findWords2(self, words: List[str]) -> List[str]:
        """
        set intersection operator
        s1.intersection(s2) <=> s1 & s2
        """
        row1, row2, row3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        res = []
        for word in words:
            w = set(word.lower())
            if w & row1 == w or w & row2 == w or w & row3 == w:
                res.append(word)
        return res

