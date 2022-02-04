"""
94. Binary Tree Inorder Traversal
Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:
Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Constraints:
The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?
"""

from typing import Optional, List


# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # DFS inorder: left -> root -> right
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

    def inorderTraversal2(self, root: Optional[TreeNode]) -> List[int]:
        """
        In inorder, the order should be
        left -> root -> right
        But when we use stack, the order should be reversed:
        right -> root -> left
        https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/1338663/Python%3A-inorder-iterative-stack-(TF-explanation)


        https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/1374069/Iterative-solution-(Stack)-in-Python.-Easy-and-fast-(-9989)
        The rule of Inorder Traversal: For each sub tree, you need visit left child of current root,
        then save root value, then visit right child of current root, and you MUST always follow this order

        When you visit each children node, if it's a parent of others children, then apply our rule again
        if it's empty- which mean it's a leaf- then add it to list res
        """
        res, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()  # the last element
            if node:
                print(f'current node: {node.val}')
                if visited:
                    res.append(node.val)
                else:  # inorder: left -> root -> right
                    stack.append((node.right, False))
                    stack.append((node, True))
                    stack.append((node.left, False))
        return res
