"""
101. Symmetric Tree
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100

Follow up: Could you solve it both recursively and iteratively?
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root.left, root.right)

    def dfs(self, l, r):
        if l and r:
            return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
        return l == r

    def isSymmetric2(self, root: Optional[TreeNode]) -> bool:
        """
        if we define function dfs(l, r) inside isSymmetric(), it's ok to not use self,
        but the above approach is preferred
        """
        def dfs(l, r):
            if l and r:
                return l.val == r.val and dfs(l.left, r.right) and dfs(l.right, r.left)
            return l is r
        return dfs(root.left, root.right)

    def isSymmetric3(self, root: Optional[TreeNode]) -> bool:
        # same pattern as problem 100, Same Tree
        stack = [(root.left, root.right)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.left, n2.right))
                stack.append((n1.right, n2.left))
            elif not n1 and not n2:
                continue
            else:
                return False
        return True
