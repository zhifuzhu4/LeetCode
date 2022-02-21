"""
229. Majority Element II
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Example 1:
Input: nums = [3,2,3]
Output: [3]

Example 2:
Input: nums = [1]
Output: [1]

Example 3:
Input: nums = [1,2]
Output: [1,2]

Constraints:
1 <= nums.length <= 5 * 10**4
-10**9 <= nums[i] <= 10**9

Follow up: Could you solve the problem in linear time and in O(1) space?
"""

from typing import List
import collections


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ct = collections.Counter(nums)
        res = []
        for k in ct:
            if ct[k] > len(nums)/3:
                res.append(k)
        return res

    def majorityElement2(self, nums: List[int]) -> List[int]:
        d = {}
        res = []
        for n in nums:
            d[n] = d.get(n, 0) + 1
        for k in d:
            if d[k] > len(nums)/3:
                res.append(k)
        return res

    def majorityElement3(self, nums: List[int]) -> List[int]:
        res = []
        vals = list(set(nums))
        for n in vals:
            if nums.count(n) > len(nums)/3:
                res.append(n)
        return res

    def majorityElement4(self, nums: List[int]) -> List[int]:
        """
        Boyer-Moore Majority Vote algorithm http://goo.gl/64Nams

        The essential concepts is you keep a counter for the majority number X.
        If you find a number Y that is not X, the current counter should deduce 1.
        The reason is that if there is 5 X and 4 Y, there would be one (5-4) more X than Y.
        This could be explained as "4 X being paired out by 4 Y".

        And since the requirement is finding the majority for more than ceiling of [n/3],
        the answer would be less than or equal to two numbers.
        So we can modify the algorithm to maintain two counters for two majorities.
        """
        candidate1, candidate2, cnt1, cnt2 = 0, 1, 0, 0
        for n in nums:
            if n == candidate1:
                cnt1 += 1
            elif n == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1, cnt1 = n, 1
            elif cnt2 == 0:
                candidate2, cnt2 = n, 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        return [x for x in (candidate1, candidate2) if nums.count(x) > len(nums)/3]
