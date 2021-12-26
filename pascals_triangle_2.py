"""
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]

Constraints:
0 <= rowIndex <= 33

Follow up: Could you optimize your algorithm to use only O(rowIndex) extra space?

# 1 0 0 0 0
# 1 1 0 0 0
# 1 2 1 0 0
# 1 3 3 1 0
# 1 4 6 4 1
使用一维数组，然后从右向左遍历每个位置，
每个位置的元素r e s [ j ] res[j]res[j] += 其左边的元素 res[j-1]

为啥不从左向右遍历呢？因为如果从左向右遍历，那么左边的元素已经更新为第 i 行的元素了，
而右边的元素需要的是第 i−1 行的元素。故从左向右遍历会破坏元素的状态。
"""

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # space complexity: O(n(n+1)/2)
        res = [[1 for _ in range(i+1)] for i in range(rowIndex+1)]
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res[-1]

    def getRow2(self, rowIndex: int) -> List[int]:
        # space complexity: O(n)
        res = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                res[j] += res[j-1]
        return res
