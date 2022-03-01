# LC 654. Maximum Binary Tree

'''
You are given an integer array nums with no duplicates. A maximum binary tree can be built recursively from nums using the following algorithm:

Create a root node whose value is the maximum value in nums.
Recursively build the left subtree on the subarray prefix to the left of the maximum value.
Recursively build the right subtree on the subarray suffix to the right of the maximum value.
Return the maximum binary tree built from nums.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return self.monostack(nums)

    # O(n^2) time | O(n) space
    def recursive(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None

        max_idx = 0

        for i in range(len(nums)):
            if nums[i] > nums[max_idx]:
                max_idx = i

        node = TreeNode(nums[max_idx])
        node.left = self.constructMaximumBinaryTree(nums[:max_idx])
        node.right = self.constructMaximumBinaryTree(nums[max_idx + 1:])

        return node

    # O(n) time | O(n) space
    def monostack(self, nums: List[int]) -> Optional[TreeNode]:
        node = TreeNode(float('inf'))
        stack = [node]

        for n in nums:
            node = TreeNode(n)

            while stack and stack[-1].val < n:
                node.left = stack.pop()

            stack[-1].right = node
            stack.append(node)

        return stack[0].right
