"""
1523. Count Odd Numbers in an Interval Range
Given two non-negative integers low and high. Return the count of odd numbers between low and high (inclusive).

Example 1:
Input: low = 3, high = 7
Output: 3
Explanation: The odd numbers between 3 and 7 are [3,5,7].

Example 2:
Input: low = 8, high = 10
Output: 1
Explanation: The odd numbers between 8 and 10 are [9].

Constraints:
0 <= low <= high <= 10^9
"""

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # get the smallest and largest odd numbers in the range,
        # then calculate the odd numbers
        odd_lb = low if low % 2 else low + 1
        odd_ub = high if high % 2 else high - 1
        return (odd_ub - odd_lb) // 2 + 1

    def countOdds2(self, low: int, high: int) -> int:
        return (high + 1) // 2 - low // 2

    def countOdds3(self, low: int, high: int) -> int:
        # same logic as solution 2 but bit operation is faster
        return ((high + 1) >> 1) - (low >> 1)
