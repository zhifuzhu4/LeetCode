"""
1779. Find Nearest Point That Has the Same X or Y Coordinate
You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

Example 1:
Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

Example 2:
Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.

Example 3:
Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.

Constraints:
1 <= points.length <= 10**4
points[i].length == 2
1 <= x, y, ai, bi <= 10**4
"""

from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        # brute force
        dis = [float('inf')] * len(points)
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                dis[i] = abs(x - a) + abs(y - b)
        min_dis = min(dis)
        res = dis.index(min_dis) if min_dis in dis and min_dis != float('inf') else -1
        return res

    def nearestValidPoint2(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist, ans = float("inf"), -1
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                man_dist = abs(a - x) + abs(b - y)
                if man_dist < min_dist:
                    ans, min_dist = i, man_dist
        return ans

    def nearestValidPoint3(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_dist = {}
        for i, (a, b) in enumerate(points):
            if a == x or b == y:
                valid_dist[i] = abs(a - x) + abs(b - y)
        return min(valid_dist, key=valid_dist.get, default=-1)
