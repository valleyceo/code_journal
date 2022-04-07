# 369. Plus One Linked List

'''
Given a non-negative integer represented as a linked list of digits, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list.

Example 1:

Input: head = [1,2,3]
Output: [1,2,4]

Example 2:

Input: head = [0]
Output: [1]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        return self.onePass(head)

    def reverseLL(self, head: ListNode) -> ListNode:
        def reverse(node) -> ListNode:
            prev = None
            curr = node

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            return prev

        def addOne(node) -> ListNode:
            head = node
            node.val += 1
            carry = 0

            while True:
                node.val += carry
                carry = 0

                if node.val == 10:
                    node.val = 0
                    carry = 1

                if carry == 0:
                    break

                if node.next:
                    node = node.next
                else:
                    node.next = ListNode(0)
                    node = node.next

            return head

        return reverse(addOne(reverse(head)))

    def onePass(self, head: ListNode) -> ListNode:
        root = ListNode(0, head)
        last_not_nine = root

        while head:
            if head.val != 9:
                last_not_nine = head

            head = head.next

        last_not_nine.val += 1
        last_not_nine = last_not_nine.next

        while last_not_nine:
            last_not_nine.val = 0
            last_not_nine = last_not_nine.next

        return root if root.val == 1 else root.next
