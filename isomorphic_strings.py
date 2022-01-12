"""
205. Isomorphic Strings
Given two strings s and t, determine if they are isomorphic (同构的）.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters.
No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Example 4:
Input: s = "bbbaaaba", t = "aaabbbba"
Output: False

Constraints:
1 <= s.length <= 5 * 10**4
t.length == s.length
s and t consist of any valid ascii character.
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            else:
                s2t[s[i]] = t[i]

            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            else:
                t2s[t[i]] = s[i]
        return True

    def isIsomorphic2(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic3(self, s: str, t: str) -> bool:
        """
        The idea is that we need to map a char to another one, for example, "egg" and "add",
        we need to constract the mapping 'e' -> 'a' and 'g' -> 'd'.
        Instead of directly mapping 'e' to 'a', another way is to mark them with same value,
        for example, 'e' -> 1, 'a'-> 1, and 'g' -> 2, 'd' -> 2, this works same.

        It's like a translator. Let's say one person speaks Spanish, and another person speaks French.
        How do we know if the two person is talking about the same thing? We can translate both Spanish and French
        to English and see if the translations are the same.
        """
        # return [s.find(i) for i in s] == [t.find(j) for j in t]
        return list(map(s.find, s)) == list(map(t.find, t))

    def isIsomorphic4(self, s: str, t: str) -> bool:
        d1, d2 = {}, {}
        for i, v in enumerate(s):
            d1[v] = d1.get(v, []) + [i]
        for i, v in enumerate(t):
            d2[v] = d2.get(v, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
