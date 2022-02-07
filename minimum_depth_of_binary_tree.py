"""
111. Minimum Depth of Binary Tree
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5

Constraints:
The number of nodes in the tree is in the range [0, 10**5].
-1000 <= Node.val <= 1000
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # recursive
        # if one of the subtrees is None, return the depth of another subtree
        # if no subtree is None, return the minimum depth of the two subtrees
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepth2(self, root: Optional[TreeNode]) -> int:
        # DFS
        if not root:
            return 0
        res, stack = float('inf'), [(root, 1)]
        while stack:
            node, level = stack.pop()
            if node and not node.left and not node.right:
                res = min(res, level)
            if node:
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
        return res

    def minDepth3(self, root: Optional[TreeNode]) -> int:
        # BFS
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))
