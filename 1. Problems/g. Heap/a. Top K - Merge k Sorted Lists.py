# 23. Merge k Sorted Lists

"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
class Data:
    def __init__(self, node: ListNode, next=None):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

# O(MN) time | O(len(M)) space
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        hArr = []
        res = ListNode(0)
        curr = res

        for node in lists:
            if node is None:
                continue

            heapq.heappush(hArr, Data(node))

        while hArr:
            data = heapq.heappop(hArr)

            if data.node.next:
                heapq.heappush(hArr, Data(data.node.next))

            curr.next = data.node
            curr = curr.next

        return res.next if res.next else None
