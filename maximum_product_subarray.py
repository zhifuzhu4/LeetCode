"""
152. Maximum Product Subarray
Given an integer array nums, find a contiguous non-empty subarray within the array
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.
A subarray is a contiguous subsequence of the array.

Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
1 <= nums.length <= 2 * 10**4
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Subproblem for the DP here would be: What is the maximum and minimum product we can get
        for a contiguous sub-array starting from the 0th to the current element?
        Why do we need to maintain the minimum product while we are asked for a maximum?
        The fact is that elements in nums can be negative, so it's possible that for some negative element
        the previous min possible product can turn the current product into a greater value.

        You have three choices to make at any position in array.
        1. You can get maximum product by multiplying the current element with maximum product calculated so far.
        (might work when current element is positive).
        2. You can get maximum product by multiplying the current element with minimum product calculated so far.
        (might work when current element is negative).
        3. Current element might be a starting position for maximum product subarray
        """
        cur_min = cur_max = res = nums[0]
        for n in nums[1:]:
            vals = [n, n*cur_min, n*cur_max]
            cur_min, cur_max = min(vals), max(vals)
            res = max(res, cur_max)
        return res
