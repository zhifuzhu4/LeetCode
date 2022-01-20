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
If the sum of a subarray is positive, it's possible to make the next value bigger,
so we keep doing it until it turns to negative.
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
        """
        Kadane’s Algorithm is an iterative dynamic programming algorithm.
        It calculates the maximum sum subarray ending at a particular position by using
        the maximum sum subarray ending at the previous position.
        """
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

    def maxSubArray2(self, nums: List[int]) -> int:
        # use dp memoisation table, time O(n), space O(n)
        n = len(nums)
        dp = [nums[0]] * n
        for i in range(1, n):
            if dp[i-1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        # the above if-else can be rewritten as
        # dp[i] = max(dp[i-1]+nums[i], nums[i])
        return max(dp)

    def maxSubArray3(self, nums: List[int]) -> int:
        # time O(n), space O(1)
        # 1) initilize both variables as nums[0]
        # 2) iterate from index-1
        cur_sum = max_sum = nums[0]
        for num in nums[1:]:
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
