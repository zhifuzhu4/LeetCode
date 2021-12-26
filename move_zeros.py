"""
283. Move Zeroes

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
1 <= nums.length <= 10**4
-2**31 <= nums[i] <= 2**31 - 1

Follow up: Could you minimize the total number of operations done?
"""

from typing import List


class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        for x in nums:
            if x:
                nums[i] = x
                i += 1
        nums[i:(n+1)] = [0] * (n - 1)

    def moveZeros2(self, nums: List[int]) -> None:
        i = 0
        for j in range(len(nums)):
            if nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
