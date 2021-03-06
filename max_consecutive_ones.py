"""
485. Max Consecutive Ones

Given a binary array nums, return the maximum number of consecutive 1's in the array.

Example 1:
Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.

Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 2

Constraints:
1 <= nums.length <= 10**5
nums[i] is either 0 or 1.

Note: similar to problem: consecutive characters
"""

from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = ans = 0
        for x in nums:
            if x:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 0
        return ans
