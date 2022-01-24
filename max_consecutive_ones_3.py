"""
1004. Max Consecutive Ones III
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 10**5
nums[i] is either 0 or 1.
0 <= k <= nums.length

Note:
https://leetcode.com/problems/max-consecutive-ones-iii/discuss/719833/Python3-sliding-window-with-clear-example-explains-why-the-soln-works
"""

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = right = 0

        for right in range(len(nums)):
            # if we encounter a 0 then we decrement k
            if nums[right] == 0:
                k -= 1
            # else no impact to k

            # if k < 0 then we need to move the left part of the window forward to try and remove the extra 0's
            if k < 0:
                # if the left one was zero then we adjust k
                if nums[left] == 0:
                    k += 1
                # regardless of whether we had a 1 or a 0 we can move left side by 1
                # if we keep seeing 1's the window still keeps moving as-is
                left += 1

        return right - left + 1
