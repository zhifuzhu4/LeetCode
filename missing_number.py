"""
268. Missing Number

Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Example 1:
Input: nums = [3,0,1]
Output: 2

Example 2:
Input: nums = [0,1]
Output: 2

Example 3:
Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8

Constraints:
n == nums.length
1 <= n <= 10**4
0 <= nums[i] <= n
All the numbers of nums are unique.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # O(n)
        for x in range(len(nums)+1):
            if x not in nums:
                return x

    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n * (n + 1) / 2 - sum(nums))

    def missingNumber3(self, nums: List[int]) -> int:
        return sum(range(len(nums)+1)) - sum(nums)

    def missingNumber4(self, nums: List[int]) -> int:
        """
        use XOR
        n ^ n = 0
        a ^ b ^ c ^ a ^ b = c
        so for all elements in [0, n], XOR all elements in nums, the one remaining is the missing one.
        range(n) contains elements in [0, n-1], so we need to initialize res = n, together we get [0, n]
        """
        n = len(nums)
        res = n
        for i in range(n):
            res ^= i
            res ^= nums[i]
        return res
