"""
424. Longest Repeating Character Replacement
You are given a string s and an integer k. You can choose any character of the string
and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:
Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.

Constraints:
1 <= s.length <= 10**5
s consists of only uppercase English letters.
0 <= k <= s.length
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Maintain a dictionary that keeps track of last 'window' characters
        # See if 'window' size minus occurrences of the most common char is <= k, if so it's valid
        # Run time is O(length of string * size of alphabet)
        # Space is O(size of alphabet)

        d = {}
        window = 0

        for i, char in enumerate(s):
            d[char] = d.get(char, 0) + 1
            if window+1 - max(d.values()) <= k:
                window += 1
            else:
                d[s[i-window]] -= 1
        return window