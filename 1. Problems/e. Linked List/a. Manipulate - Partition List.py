# LC 86. Partition List

'''
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example 1:

Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]

Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # O(n) time | O(1) space
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        larger_head = larger = ListNode(0)
        lower_head = lower = ListNode(0)

        while head:
            if head.val < x:
                lower.next = head
                lower = lower.next
            else:
                larger.next = head
                larger = larger.next


            head = head.next

        larger.next = None
        lower.next = larger_head.next
        return lower_head.next
