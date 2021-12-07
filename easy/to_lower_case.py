"""
709. To Lower Case

Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.

Example 1:
Input: s = "Hello"
Output: "hello"

Example 2:
Input: s = "here"
Output: "here"

Example 3:
Input: s = "LOVELY"
Output: "lovely"

Constraints:
1 <= s.length <= 100
s consists of printable ASCII characters.

Note:
ASCII (American Standard Code for Information Interchange) is a character encoding standard
for electronic communication. ASCII codes represent text in computers, telecommunications equipment, and other devices

order: UPPER CASE (A-Z), 6 special characters, lower case (a-z)
ord('A') -> 65
ord('Z') -> 90
ord('a') -> 97
ord('z') -> 122
'A' < 'Z' < 'a' < 'z'
"""

class Solution:
    def toLowerCase(self, s: str) -> str:
        return "".join(chr(ord(c) + 32) if 65 <= ord(c) <= 90 else c for c in s)

    def toLowerCase2(self, s: str) -> str:
        return "".join(chr(ord(c) + 32) if "A" <= c <= "Z" else c for c in s)

    def toLowerCase3(self, s: str) -> str:
        return s.lower()
