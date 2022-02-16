"""
24. Swap Nodes in Pairs
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]

Constraints:
The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # iteratively
        if not head or not head.next:
            return head
        second = head.next
        pre = ListNode(0)
        while head and head.next:
            nxt = head.next
            head.next = nxt.next
            nxt.next = head
            pre.next = nxt
            head = head.next
            pre = nxt.next
        return second

    def swapPairs2(self, head):
        # recursively
        if not head or not head.next:
            return head
        second = head.next
        head.next = self.swapPairs(second.next)
        second.next = head
        return
