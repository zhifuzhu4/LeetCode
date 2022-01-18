"""
203. Remove Linked List Elements
Given the head of a linked list and an integer val,
remove all the nodes of the linked list that has Node.val == val, and return the new head.

Example 1:
Input: head = [1,2,6,3,4,5,6], val = 6
Output: [1,2,3,4,5]

Example 2:
Input: head = [], val = 1
Output: []

Example 3:
Input: head = [7,7,7,7], val = 7
Output: []

Constraints:
The number of nodes in the list is in the range [0, 10**4].
1 <= Node.val <= 50
0 <= val <= 50
"""
from typing import Optional

# Definition for single-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # this method starts removing elements from head.next, so we need to consider the edge case that:
        # the head node, and any number of nodes immediately after it have the target value.
        while head and head.val == val:
            head = head.next

        cur = head
        while cur:
            if cur.next and cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

    def removeElements2(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # this method creates a dummy head to deal with the edge case discussed above
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next
