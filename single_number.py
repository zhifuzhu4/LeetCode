"""
136. Single Number
Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1

Constraints:
1 <= nums.length <= 3 * 10**4
-3 * 10**4 <= nums[i] <= 3 * 10**4
Each element in the array appears twice except for one element which appears only once.
"""

from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for i, v in enumerate(nums):
            d[v] = d.get(v, 0) + 1
        for k in d:
            if d[k] == 1:
                return k

    def singleNumber2(self, nums: List[int]) -> int:
        """
        for any number n
        n ^ 0 = n
        n ^ n = 0
        So… if n is the single number
        n1 ^ n1 ^ n2 ^ n2 … nx ^ nx ^ n
        = (n1^n1) ^ (n2^n2) … (nx^nx) ^ n
        = 0 ^ 0 ^ … ^ 0 ^ n
        = n
        """
        res = 0
        for n in nums:
            res ^= n
        return res

    def singleNumber3(self, nums: List[int]) -> int:
        return 2*sum(set(nums)) - sum(nums)

    def singleNumber4(self, nums: List[int]) -> int:
        """
        nums = [4,1,2,1,2]
        collections.Counter(nums) -> Counter({1: 2, 2: 2, 4: 1})
        collections.Counter(nums).most_common() -> [(1, 2), (2, 2), (4, 1)]
        """
        return collections.Counter(nums).most_common()[-1][0]
