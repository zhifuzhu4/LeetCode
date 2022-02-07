"""
617. Merge Two Binary Trees
You are given two binary trees root1 and root2.
Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped
while the others are not. You need to merge the two trees into a new binary tree. The merge rule is that
if two nodes overlap, then sum node values up as the new value of the merged node.
Otherwise, the NOT null node will be used as the node of the new tree.

Return the merged tree.

Note: The merging process must start from the root nodes of both trees.

Example 1:
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]

Example 2:
Input: root1 = [1], root2 = [1,2]
Output: [2,2]

Constraints:
The number of nodes in both trees is in the range [0, 2000].
-10**4 <= Node.val <= 10**4
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursive
        if root1 and root2:
            root = TreeNode(root1.val + root2.val)
            root.left = self.mergeTrees(root1.left, root2.left)
            root.right = self.mergeTrees(root1.right, root2.right)
            return root
        else:
            return root1 or root2

    def mergeTrees2(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # iterative
        if not root1 or not root2:
            return root1 or root2
        stack = [[root1, root2]]
        while stack:
            cur = stack.pop()
            if not cur[0] or not cur[1]:
                continue
            cur[0].val += cur[1].val
            if not cur[0].left:
                cur[0].left = cur[1].left
            else:
                stack.append([cur[0].left, cur[1].left])
            if not cur[0].right:
                cur[0].right = cur[1].right
            else:
                stack.append([cur[0].right, cur[1].right])
        return root1
