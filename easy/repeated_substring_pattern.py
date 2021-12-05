"""
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it
and appending multiple copies of the substring together.

Example 1:
Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.

Example 2:
Input: s = "aba"
Output: false

Example 3:
Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

Constraints:
1 <= s.length <= 104
s consists of lowercase English letters.

Note:
If the string S has repeated block, it could be described in terms of pattern.
S = SpSp (For example, S has two repeatable block at most)
If we repeat the string, then SS=SpSpSpSp.
Destroying first and the last pattern by removing each character, we generate a new S2=SxSpSpSy.

If the string has repeatable pattern inside, S2 should have valid S in its string.
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if not s:
            return False
        # the above two lines are necessary if we use s2.find(s) since ''.find('') -> 0
        # when s == '', s[1] throws an exception, but s[1:-1] will not.
        s2 = (s*2)[1:-1]
        return s2.find(s) != -1

    def repeatedSubstringPattern2(self, s: str) -> bool:
        return s in (s + s)[1:-1]

    def repeatedSubstringPattern3(self, s: str) -> bool:
        # TODO: study this solution
        # https://leetcode.com/problems/repeated-substring-pattern/discuss/826121/Python-2-solutions1-oneliner-explained
        n = len(s)
        for i in range(1, n//2+1):
            if n % i == 0 and s[:i] * (n//i) == s:
                return True
        return False
