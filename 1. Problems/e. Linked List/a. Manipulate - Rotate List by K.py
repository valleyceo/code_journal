# 61. Rotate List

'''
Given the head of a linked list, rotate the list to the right by k places.

Example 1:

Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:

Input: head = [0,1,2], k = 4
Output: [2,0,1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# O(n) time | O(1) space
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head

        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1

        curr.next = head
        k = k % n
        curr = head

        for _ in range(n - k - 1):
            curr = curr.next

        newHead = curr.next
        curr.next = None

        return newHead
