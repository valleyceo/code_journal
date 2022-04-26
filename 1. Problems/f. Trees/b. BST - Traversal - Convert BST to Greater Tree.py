# LC 538. Convert BST to Greater Tree

'''
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.iterative(root)

    def recursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def revInorder(node):
            nonlocal moving_sum

            if node is None:
                return

            revInorder(node.right)

            moving_sum += node.val
            node.val = moving_sum

            revInorder(node.left)


        moving_sum = 0
        revInorder(root)
        return root

    def iterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        moving_sum = 0
        curr = root
        stack = []

        while stack or curr:

            while curr is not None:
                stack.append(curr)
                curr = curr.right

            curr = stack.pop()

            moving_sum += curr.val
            curr.val = moving_sum

            curr = curr.left

        return root
