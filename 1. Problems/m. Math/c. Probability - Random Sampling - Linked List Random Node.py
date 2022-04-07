# LC 382. Linked List Random Node

'''
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.

Example 1:

Input
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
Output
[null, 1, 3, 2, 2, 3]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Reservoir Sampling, O(1) time | O(N) space, unknown size
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.root = head

    def getRandom(self) -> int:
        scope = 1
        chosen_val = 0
        curr = self.root

        while curr:
            if random.random() < 1 / scope:
                chosen_val = curr.val

            scope += 1
            curr = curr.next

        return chosen_val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
