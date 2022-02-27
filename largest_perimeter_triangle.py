"""
976. Largest Perimeter Triangle
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area,
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

Example 1:
Input: nums = [2,1,2]
Output: 5

Example 2:
Input: nums = [1,2,1]
Output: 0

Constraints:
3 <= nums.length <= 10**4
1 <= nums[i] <= 10**6
"""

from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # sort the list in descending order, and starting from the largest number,
        # if n1 < n2 + n3, the three numbers can form a triangle
        nums.sort(reverse=True)
        # nums = sorted(nums)[::-1]
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
        return 0
