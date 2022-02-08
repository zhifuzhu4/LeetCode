""""
653. Two Sum IV - Input is a BST
Given the root of a Binary Search Tree and a target number k,
return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Example 2:
Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:
The number of nodes in the tree is in the range [1, 10**4].
-10**4 <= Node.val <= 10**4
root is guaranteed to be a valid binary search tree.
-10**5 <= k <= 10**5
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        # DFS get the full list of nodes' values first, not efficient
        def preorderTraversal(node):
            return [node.val] + preorderTraversal(node.left) + preorderTraversal(node.right) if node else []
        nodes = preorderTraversal(root)
        for i in range(len(nodes)):
            if k - nodes[i] in nodes[i+1:]:
                return True
        return False

    def findTarget2(self, root: Optional[TreeNode], k: int) -> bool:
        # DFS gives us a linear traversal over each node.
        # Only need to keep track of what we've seen and what we need to visit: O(N) time & space.
        stack, seen = [root], set()
        while stack:
            node = stack.pop()
            if k - node.val in seen:
                return True
            seen.add(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False
