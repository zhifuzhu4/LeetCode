"""
867. Transpose Matrix
Given a 2D integer array matrix, return the transpose of matrix.
The transpose of a matrix is the matrix flipped over its main diagonal,
switching the matrix's row and column indices.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 10**5
-10**9 <= matrix[i][j] <= 10**9
"""

from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]

    def transpose2(self, matrix: List[List[int]]) -> List[List[int]]:
        return list(zip(*matrix))

    def transpose3(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = []
        for i in range(n):
            new_row = []
            for j in range(m):
                new_row.append(matrix[j][i])
            res.append(new_row)
        return res

    def transpose4(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(matrix[0])
        for i in range(n):
            res.append([row[i] for row in matrix])
        return res
