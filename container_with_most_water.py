"""
11. Container With Most Water
You are given an integer array height of length n.
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 10**5
0 <= height[i] <= 10**4
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        If height[L] < height[R], move L, else move R. Say height[0] < height[5],
        area of (0, 4), (0, 3), (0, 2), (0, 1) will be smaller than (0, 5), so no need to try them.

        https://leetcode.com/problems/container-with-most-water/discuss/1069746/JS-Python-Java-C%2B%2B-or-2-Pointer-Solution-w-Visual-Explanation-or-beats-100
        """
        left, right = 0, len(height)-1
        res = 0
        while left < right:
            if height[left] > height[right]:
                res = max(res, height[right] * (right-left))
                right -= 1
            else:
                res = max(res, height[left] * (right - left))
                left += 1
        return res
