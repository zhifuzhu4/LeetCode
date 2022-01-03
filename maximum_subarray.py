"""
53. Maximum Subarray

Given an integer array nums,
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23

Constraints:
1 <= nums.length <= 10**5
-10**4 <= nums[i] <= 10**4

Follow up: If you have figured out the O(n) solution,
try coding another solution using the divide and conquer approach, which is more subtle.

Note:
If the sum of a subarray is positive, it has possible to make the next value bigger,
so we keep do it until it turn to negative.
If the sum is negative, it has no use to the next element, so we break.
it is a game of sum, not the elements.

明显的DP方法去解决。
通过构建一个和原长一样长的数组， dp 数组的含义是以 dp[i] 为结尾的最大子数组的和。

状态转移公式：
dp[i] = dp[i - 1] + nums[i] 当 nums[i] >= 0 。
dp[i] = nums[i] 当 nums[i] < 0 。

题目求的最大子数组的和，就是 dp 数组的最大值。


贪心，到当前位置并且包括当前数字的最大子数组，可以是这个数自己，或者自己加上之前上到上一个数的最大子数组
cur = max(nums[i], cur + nums[i])

TODO: divide and conquer solution
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def maxSubArray(self, nums: List[int]) -> int:
        res = cur = nums[0]
        for n in nums[1:]:
            cur = max(cur+n, n)
            res = max(res, cur)
        return res