# 19. Remove Nth Node From End of List

'''
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
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode(-1, head)
        fast = pre
        slow = pre

        for _ in range(n):
            if fast:
                fast = fast.next
            else:
                return None

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return pre.next
