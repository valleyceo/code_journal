# LC 82. Remove Duplicates from Sorted List II

'''
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

Example 1:

Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]

Example 2:

Input: head = [1,1,1,2,3]
Output: [2,3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = curr = ListNode(0)
        curr.next = head

        while curr.next:
            count = 1
            node = curr.next
            while node.next and node.val == node.next.val:
                node = node.next
                count += 1

            if count == 1:
                curr = curr.next
            else:
                curr.next = node.next

        return res.next
