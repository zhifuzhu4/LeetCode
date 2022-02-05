"""
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Constraints:
The number of nodes in the tree is in the range [0, 10**4].
-100 <= Node.val <= 100
"""

from typing import Optional
import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

    def maxDepth2(self, root: Optional[TreeNode]) -> int:
        # DFS
        res = 0
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if not node:
                res = max(res, level)
            else:
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

    def maxDepth3(self, root: Optional[TreeNode]) -> int:
        # BFS + deque
        if not root:
            return 0
        queue = collections.deque([(root, 1)])  # here the 2nd number is level
        while queue:
            cur, val = queue.popleft()
            if cur.left:
                queue.append((cur.left, val+1))
            if cur.right:
                queue.append((cur.right, val+1))
        return val

    def maxDepth4(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res, level = [], [root]
        while level:
            res.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]
        return len(res)
