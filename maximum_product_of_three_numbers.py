"""
628. Maximum Product of Three Numbers
Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:
Input: nums = [1,2,3]
Output: 6

Example 2:
Input: nums = [1,2,3,4]
Output: 24

Example 3:
Input: nums = [-1,-2,-3]
Output: -6

Constraints:
3 <= nums.length <= 10**4
-1000 <= nums[i] <= 1000
"""

from typing import List


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # time complexity, O(nlogk), where k = 3 -> O(n)
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])

    def maximumProduct2(self, nums: List[int]) -> int:
        # the same idea as the above but without sort()
        min1 = min2 = float('inf')  # min1 < min2
        max3 = max2 = max1 = float('-inf')  # max3 < max2 < max1
        for n in nums:
            if n > max1:
                max3, max2, max1 = max2, max1, n
            elif n > max2:
                max3, max2 = max2, n
            elif n > max3:
                max3 = n

            if n < min1:
                min1, min2 = n, min1
            elif n < min2:
                min2 = n
        return max(max3*max2*max1, min1*min2*max1)
