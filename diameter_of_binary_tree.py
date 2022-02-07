"""
543. Diameter of Binary Tree
Given the root of a binary tree, return the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes in a tree.
This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.

Example 1:
Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].

Example 2:
Input: root = [1,2]
Output: 1

Constraints:
The number of nodes in the tree is in the range [1, 10**4].
-100 <= Node.val <= 100
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        The height of a node is the number of edges on the longest downward path between that node and a leaf.
        dfs function calculates the height of the node, i.e, the longest downward path between the node and a leaf.
        For a node, the length of longest path going through the node is the sum of left child's height
        plus right child's height.
        For each node in the binary tree, we calculate the length of the longest length going through the node,
        the maximum length is the diameter of the binary tree according to the definition --The diameter of a
        binary tree is the length of the longest path between any two nodes in a tree.
        https://leetcode.com/problems/diameter-of-binary-tree/discuss/574778/Python3-dfs-Bottom-up-to-calculate-the-height-of-the-node
        """
        self.diameter = 0
        self.dfs(root)
        return self.diameter

    def dfs(self, node):
        # base case:
        if not node:
            return 0
        # recursive cases
        left_height = self.dfs(node.left)
        right_height = self.dfs(node.right)
        self.diameter = max(self.diameter, left_height + right_height)
        return max(left_height, right_height) + 1
