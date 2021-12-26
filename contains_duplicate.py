"""
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
1 <= nums.length <= 10**5
-10**9 <= nums[i] <= 10**9
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    def containsDuplicate2(self, nums: List[int]) -> bool:
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 1
            else:
                freq[x] += 1
        return max(freq.values()) > 1
