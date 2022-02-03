"""
108. Convert Sorted Array to Binary Search Tree
Given an integer array nums where the elements are sorted in ascending order,
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which
the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:
Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.

Constraints:
1 <= nums.length <= 10**4
-10**4 <= nums[i] <= 10**4
nums is sorted in a strictly increasing order.
"""

from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        The idea is to find the root first, then recursively build each left and right subtree

        1. create a new node with the middle value of the array
        2. for the left child, call the function again - passing the the left half of the array
        3. for the right child, call the function again - passing the right half of the array
        4. important to not include the middle value when passing in these new subarrays
        5. this continues until the subarrays are 0, where we can no longer create any new nodes
        6. once all the children are filled we can return the node

        The middle element is always the root. In case there are two middle elements, either can be the root.
        e.g., [1, 2, 3, 4, 5], mid = 5 // 2 -> 2, nums[mid] = nums[2] = 3
        [1, 2, 3, 4, 5, 6], mid = 6 // 2 -> 3, nums[mid] = nums[3] = 4
        more details can be found at:
        https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/1363643/Python3-Two-Solutions-Explained-with-Diagrams
        """
        #
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root
