"""
383. Ransom Note

Given two stings ransomNote and magazine,
return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:
1 <= ransomNote.length, magazine.length <= 10**5
ransomNote and magazine consist of lowercase English letters.
"""

from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for x in set(ransomNote):
            if ransomNote.count(x) > magazine.count(x):
                return False
        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        for x in ransomNote:
            if x in magazine:
                magazine = magazine.replace(x, '', 1)
            else:
                return False
        return True

    def canConstruct3(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransom_ct = Counter(ransomNote)
        magazine_ct = Counter(magazine)
        for key in ransom_ct:
            if ransom_ct[key] > magazine_ct[key]:
                return False
        return True

    def canConstruct4(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        ransom_d, magazine_d = {}, {}
        for x in ransomNote:
            ransom_d[x] = ransom_d.get(x, 0) + 1
        for x in magazine:
            magazine_d[x] = magazine_d.get(x, 0) + 1

        for x in ransom_d:
            if x not in magazine_d:
                return False
            elif ransom_d[x] > magazine_d[x]:
                return False
        return True
