"""
530. Minimum Absolute Difference in BST
Given the root of a Binary Search Tree (BST), return the minimum absolute difference
between the values of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Constraints:
The number of nodes in the tree is in the range [2, 10**4].
0 <= Node.val <= 10**5

Note: This question is the same as 783
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        Because of the properties of BST, inorder traversal gives the sorted node values
        Therefore, inorder traversal is the most efficient.
        Otherwise, we can use any traversal approaches but need to sort the values.
        """
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []
        lst = inorder(root)
        res = lst[-1]
        for i in range(len(lst)-1):
            res = min(res, abs(lst[i] - lst[i+1]))
        return res

    def getMinimumDifference2(self, root: Optional[TreeNode]) -> int:
        # preorder traverl + sort()
        def preorder(node):
            return [node.val] + preorder(node.left) + preorder(node.right) if node else []
        lst = preorder(root)
        lst.sort()
        res = lst[-1]
        for i in range(len(lst)-1):
            res = min(res, abs(lst[i] - lst[i+1]))
        return res
