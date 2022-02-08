"""
100. Same Tree
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example 1:
Input: p = [1,2,3], q = [1,2,3]
Output: true

Example 2:
Input: p = [1,2], q = [1,null,2]
Output: false

Example 3:
Input: p = [1,2,1], q = [1,1,2]
Output: false

Constraints:
The number of nodes in both trees is in the range [0, 100].
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
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recursive
        # return p is q:  returns True if p==None and q==None else False
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # DFS with stack
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2 and node1.val == node2.val:
                # the order of left and right does not matter, either way works fine
                # to avoid confusion, use current order so pop works from left to right
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
            elif not node1 and not node2:
                continue
            else:
                return False
        return True

    def isSameTree3(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS with queue
        queue = [(p, q)]
        while queue:
            node1, node2 = queue.pop(0)
            if node1 and node2 and node1.val == node2.val:
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            elif not node1 and not node2:
                continue
            else:
                return False
        return True
