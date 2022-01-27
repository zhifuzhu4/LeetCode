"""
206. Reverse Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:
The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

TODO: study both iterative solutions and recursive solution
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Below are the steps:
            1) initialize nxt to be the node after cur. i.e(nxt = cur.next).
            2) make cur.next point to prev (next node pointer).
            3) make prev now point to (one node ahead) the cur node.
            4) move cur also one node ahead to nxt.
        """
        prev,  cur = None, head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        the order of multiple assignments maters
        Basically how multiple assignment works is:
        1. The right hand side of the equation is evaluated first simultaneously and stored into memory,
        which is good as we do not need to manually create temp variables ourselves.
        2. Each of the items on the left hand side is assigned sequentially (from left to right).
        This is the key issue, the assignment is not simultaneous but rather sequential.
        Therefore, cur.next, prev, cur = prev, cur, cur.next works
        but prev, cur, cur.next = cur, cur.next, prev does not work
        """
        prev, cur = None, head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        return prev

    def reverseList3(self, head: Optional[ListNode], prev=None) -> Optional[ListNode]:
        # recursive
        if head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
            return self.reverseList3(head, prev)
        else:
            return prev
