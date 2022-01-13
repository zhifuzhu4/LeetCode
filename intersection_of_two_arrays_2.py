"""
350. Intersection of Two Arrays II
Given two integer arrays nums1 and nums2, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays
and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk,
and the memory is limited such that you cannot load all elements into the memory at once?

TODO: study answers for follow ups at
https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/1468295/Python-2-approaches-and-3-Follow-up-Questions-Clean-and-Concise
"""

from typing import List


class Solution:
    def intersect1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in nums1:
            if x in nums2:
                res.append(x)
                nums2.remove(x)
        return res

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # two pointers
        nums1.sort()
        nums2.sort()
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                res.append(nums1[i])
                i += 1
                j += 1
        return res
