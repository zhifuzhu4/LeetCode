"""
234. Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome.

Example 1:
Input: head = [1,2,2,1]
Output: true

Example 2:
Input: head = [1,2]
Output: false

Constraints:
The number of nodes in the list is in the range [1, 10**5].
0 <= Node.val <= 9

Follow up: Could you do it in O(n) time and O(1) space?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Two steps
        1. Reverse the first half while finding the middle (slow).
        2. Compare the reversed first half with the second half.
        """

        fast = slow = head
        # find the mid node
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the second half
        rev = None
        while slow:
            nxt = slow.next
            slow.next = rev
            rev = slow
            slow = nxt

        # compare the first and second half nodes
        while rev and head:  # while rev and head:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next
        return True

    def isPalindrome2(self, head: Optional[ListNode]) -> bool:
        # 1. Get the midpoint (slow)
        slow = fast = head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        # 2. Push the second half into the stack
        stack = [slow.val]
        while slow.next:
            slow = slow.next
            stack.append(slow.val)

        # 3. Comparison
        while stack:
            if stack.pop() != head.val:
                return False
            head = head.next
        return True

    def isPalindrome3(self, head: Optional[ListNode]) -> bool:
        # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
        rev = None
        # initially slow and fast are the same, starting from head
        slow = fast = head
        while fast and fast.next:
            # fast traverses faster and moves to the end of the list if the length is odd
            fast = fast.next.next

            # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next),
            # hence the re-assignment of slow would not affect rev (rev = slow)
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        # compare the reversed first half with the second half
        while rev and rev.val == slow.val:
            slow = slow.next
            rev = rev.next

        # if equivalent then rev become None, return True; otherwise return False
        return not rev

    def isPalindrome4(self, head: Optional[ListNode]) -> bool:
        # if O(1) space is not required
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums == nums[::-1]
