"""
33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown
pivot index k (1 <= k < nums.length) such that the resulting array
is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target,
return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

Example 3:
Input: nums = [1], target = 0
Output: -1

Constraints:
1 <= nums.length <= 5000
-10**4 <= nums[i] <= 10**4
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-10**4 <= target <= 10**4

TODO: study other solutions that do not have so many corner cases, like
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14419/Pretty-short-C%2B%2BJavaRubyPython
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        In this solution, right = mid - 1 and left = mid + 1 are essential
        without the +/-1, we will have the LTE issue
        """
        left, right = 0, len(nums)-1
        while left <= right:
            # the above <= is esential, < does not work, e.g., nums=[4,5,6,7,0,1,2], target=0
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid

            # pivot at right, and left side is strictly increasing
            # e.g, [3, 4, 5, 6, 7, 1, 2]
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # pivot at left, and right side is strictly increasing
                # e.g, [6, 7, 1, 2, 3, 4, 5]
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1