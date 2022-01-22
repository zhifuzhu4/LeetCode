"""
15. 3Sum

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-10**5 <= nums[i] <= 10**5
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        set_name.add(x), x must be hashable, (1, 2, 3) works, but not [1, 2, 3]
        """
        nums.sort()
        n = len(nums)
        res = set()
        for i in range(n):
            left, right = i+1, n-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return [list(x) for x in res]

    def threeSum2(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        nums.sort()

        for i in range(n - 2):
            # Since the list is sorted, if nums[i] > 0, then all nums[j] with j > i are positive as well,
            # and we cannot have three positive numbers sum up to 0. Return immediately.
            if nums[i] > 0:
                break

            # The nums[i] == nums[i-1] condition helps us avoid duplicates. E.g., given [-1, -1, 0, 0, 1],
            # when i = 0, we see [-1, 0, 1] works. Now at i = 1, since nums[1] == -1 == nums[0], we avoid
            # this iteration and thus avoid duplicates. The i > 0 condition is to avoid negative index,
            # i.e., when i = 0, nums[i-1] = nums[-1] and you don't want to skip this iteration when nums[0] == nums[-1]
            # what about [0, 0, 0]?
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Classic two pointer solution
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0:  # sum too small, move left ptr
                    left += 1
                elif s > 0:  # sum too large, move right ptr
                    left -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    # we need to skip elements that are identical to our
                    # current solution, otherwise we would have duplicated triples
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res
