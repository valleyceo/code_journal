# 272. Closest Binary Search Tree Value II

'''
Given the root of a binary search tree, a target value, and an integer k, return the k values in the BST that are closest to the target. You may return the answer in any order.

You are guaranteed to have only one unique set of k values in the BST that are closest to the target.

Example 1:

Input: root = [4,2,5,1,3], target = 3.714286, k = 2
Output: [4,3]

Example 2:

Input: root = [1], target = 0.000000, k = 1
Output: [1]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        self.queue = deque()
        self.k = k
        self.target = target
        self.traverse(root)

        return self.queue


    def traverse(self, node):
        if node is None:
            return

        self.traverse(node.left)

        if len(self.queue) == self.k:
            if abs(self.queue[0] - self.target) < abs(node.val - self.target):
                return
            else:
                self.queue.popleft()

        self.queue.append(node.val)

        self.traverse(node.right)
