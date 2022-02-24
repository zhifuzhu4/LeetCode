"""
1380. Lucky Numbers in a Matrix
Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

Example 1:
Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 2:
Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:
Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

Constraints:
m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 10**5.
All elements in the matrix are distinct.
"""

from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        """
        Time complexity: O(m * n)
        Space complexity: O(m + n)
        zip(*matrix) -> get the transpose of matrix
        *matrix decomposes it into separate lists each representing a row
         e.g., matrix =[[1,2], [3, 4]] *matrix returns two lists [1,2] and [3, 4]
        zip([1, 2], [3, 4]) returns two lists of [1, 3] and [2, 4] which are the columns of the matrix

        * iterable unpacking operator
        ** dictionary unpacking operator
        https://www.python.org/dev/peps/pep-0448/

        return list(set(map(min, matrix)) & set(map(max, zip(*matrix))))
        """
        return list({min(row) for row in matrix} & {max(col) for col in zip(*matrix)})
