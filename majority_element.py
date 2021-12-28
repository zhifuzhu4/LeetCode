"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than n/2 times.
You may assume that the majority element always exists in the array.

Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2

Constraints:
n == nums.length
1 <= n <= 5 * 10**4
-2**31 <= nums[i] <= 2**31 - 1

Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for x in nums:
            d[x] = d.get(x, 0) + 1
            if d[x] > len(nums)/2:
                return x

    def majorityElement2(self, nums: List[int]) -> int:
        candidate, cnt = nums[0], 0
        for num in nums:
            if num == candidate:
                cnt += 1
            elif cnt == 0:
                candidate, cnt = num, 1
            else:
                cnt -= 1
        return candidate

    def majorityElement3(self, nums: List[int]) -> int:
        vals = list(set(nums))
        for val in vals:
            if nums.count(val) > len(nums)/2:
                return val
