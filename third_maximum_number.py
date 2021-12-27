"""
414. Third Maximum Number

Given an integer array nums, return the third distinct maximum number in this array.
If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [3,2,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2.
The third distinct maximum is 1.

Example 2:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 3:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Constraints:
1 <= nums.length <= 10**4
-2**31 <= nums[i] <= 2**31 - 1

Follow up: Can you find an O(n) solution?

set operation has time complecity of O(n)
"""

from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        res = sorted(list(set(nums)))
        return res[-3] if len(res) >= 3 else res[-1]

    def thirdMax2(self, nums: List[int]) -> int:
        nums_set = set(nums)
        if len(nums_set) < 3:
            return max(nums_set)
        nums_set.remove(max(nums_set))
        nums_set.remove(max(nums_set))
        return max(nums_set)

    def thirdMax3(self, nums: List[int]) -> int:
        first, second, third = -float('inf'), -float('inf'), -float('inf')
        for x in nums:
            if x > first:
                first, second, third = x, first, second
            elif second < x < first:
                second, third = x, second
            elif third < x < second:
                third = x
        return third if third != -float('inf') else first
