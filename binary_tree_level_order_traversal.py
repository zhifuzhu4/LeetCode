"""
102. Binary Tree Level Order Traversal
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:
Input: root = [1]
Output: [[1]]

Example 3:
Input: root = []
Output: []

Constraints:
The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        level is a list of the nodes in the current level.
        Keep appending a list of the values of these nodes to ans and then updating level with
        all the nodes in the next level (kids) until it reaches an empty level.
        https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33464/5-6-lines-fast-python-solution-(48-ms)
        """
        if not root:
            return []
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return res
