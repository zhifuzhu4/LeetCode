"""
19. Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

Constraints:
The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?
"""

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # https://leetcode.com/problems/remove-nth-node-from-end-of-list/discuss/612328/PythonGo-O(n)-by-two-pointers-w-Visualization
        slow, fast = head, head

        # let the fast pointer move n steps ahead of the slow pointer
        for _ in range(n):
            fast = fast.next

        # in constaints, 1 <= n <= sz, if n == sz = len(List), we need to delete the first node
        if not fast:
            return head.next

        # then advance both fast and slow now they are nth postions apart
        # when fast gets to None, slow will be just before the item to be deleted
        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return head
