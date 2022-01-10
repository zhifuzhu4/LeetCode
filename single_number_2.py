"""
137. Single Number II

Given an integer array nums where every element appears three times except for one,
which appears exactly once. Find the single element and return it.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,3,2]
Output: 3

Example 2:
Input: nums = [0,1,0,1,0,1,99]
Output: 99

Constraints:
1 <= nums.length <= 3 * 10**4
-2**31 <= nums[i] <= 2**31 - 1
Each element in nums appears exactly three times except for one element which appears once.

TODO: study the bit solution
"""

from typing import List
import collections


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for x in d:
            if d[x] == 1:
                return x

    def singleNumber2(self, nums: List[int]) -> int:
        return collections.Counter(nums).most_common()[-1][0]

    def singleNumber3(self, nums: List[int]) -> int:
        return (3*sum(set(nums)) - sum(nums)) // 2

    def singleNumber4(self, nums: List[int]) -> int:
        single = 0
        for i in range(32):
            count = 0
            for num in nums:
                if num & (1 << i) == (1 << i):
                    count += 1
            single |= (count % 3) << i
        return single if single < (1 << 31) else single - (1 << 32)


