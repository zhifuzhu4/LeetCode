"""
118. Pascal's Triangle

Given an integer numRows, return the first numRows of Pascal's triangle.

Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]

Constraints:
1 <= numRows <= 30

Note:
    create the list for results first, then get the values for entries in the middle of the triangle.
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1 for _ in range(i)] for i in range(1, numRows+1)]
        for i in range(2, numRows):
            for j in range(1, i):
                res[i][j] = res[i-1][j-1] + res[i-1][j]
        return res
