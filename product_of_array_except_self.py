"""
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 10**5
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity analysis.)

Note:
product of array except nums[i] = product of numbers to the left of nums[i] * product of numbers to the right of nums[i]
Please note that nums[0] doesn't have elements to its left, and nums[n-1] doesn't have elements to its right. Thus
left_product[0] = 1;
right_product[n - 1] = 1;
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Space-Optimized Prefix & Suffix Products
        n = len(nums)
        res = [1] * n

        # res[i] as product of elements to the left of nums[i].
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        # res[i] multiply product of elements to the right of nums[i].
        right_product = 1
        for i in range(n-1, -1, -1):
            res[i] *= right_product
            right_product *= nums[i]
        return res

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        """
            Space-Optimized Prefix & Suffix Products in One-Pass
            The above process can be done in single pass as well. We were first calculating prefix product
            in one loop and then multiplying it with suffix product in another loop.
            These two process are independent of each other and can be done in the same loop.
            We just need to keep another prefix product variable similar to suffix_prod in previous approach.

            We iterate from start and keep calculating prefix product & update corresponding ans[i]
            & at the same time we can calculate keep calculating suffix product from the end & update ans[n-1-i].

            Note that the final result would be product of array except self because
            we only update & multiply pre with nums[i] after updating ans[i] and similarly for suf.
        """
        res, suf, pre = [1]*len(nums), 1, 1
        for i in range(len(nums)):
            res[i] *= pre               # prefix product from one end
            pre *= nums[i]
            res[-1-i] *= suf            # suffix product from other end
            suf *= nums[-1-i]
        return res
