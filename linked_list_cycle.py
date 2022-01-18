"""
141. Linked List Cycle
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again
by continuously following the next pointer. Internally, pos is used to denote the index of the node
that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.

Constraints:
The number of the nodes in the list is in the range [0, 10**4].
-10**5 <= Node.val <= 10**5
pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""

from typing import Optional


# Definition for single-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # two pointers
        # fast is moving faster than slow, so it will be the first one to reach the end of linked list
        # if it does not contain cycle. If it reaches the end, while loop is exited and will return False.
        if not head:
            return False

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # both if conditions work well
            # if low is fast <==> if slow == fast
            if slow is fast:
                return True
        return False


    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # two pointers
        """
        https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare
        Floyd's tortoise and hare
        Floyd's cycle-finding algorithm is a pointer algorithm that uses only two pointers,
        which move through the sequence at different speeds. It is also called the "tortoise and the hare algorithm",
        alluding to Aesop's fable of The Tortoise and the Hare.

        https://docs.python.org/3/glossary.html#term-eafp
        EAFP: Easier to ask for forgiveness than permission. This common Python coding style assumes
        the existence of valid keys or attributes and catches exceptions if the assumption proves false.
        This clean and fast style is characterized by the presence of many try and except statements.
        The technique contrasts with the LBYL (look before you leap) style common to many other languages such as C.
        """
        try:
            slow, fast = head, head.next
            # make sure fast = head.next, instead of slow, fast = head, head
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False
