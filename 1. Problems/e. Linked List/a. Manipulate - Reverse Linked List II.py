# LC 92. Reverse Linked List II

'''
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

Example 1:

Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]

Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time | O(1) space
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if head is None:
            return head

        prev = None
        curr = head

        for _ in range(left - 1):
            prev = curr
            curr = curr.next

        rev_prev = prev
        rev_tail = curr

        for _ in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        if rev_prev:
            rev_prev.next = prev
        else:
            head = prev

        rev_tail.next = curr

        return head
