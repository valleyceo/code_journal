# LC 114. Flatten Binary Tree to Linked List

'''
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:

Input: root = []
Output: []

Example 3:

Input: root = [0]
Output: [0]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.morrisTraversalSolution(root)

    def morrisTraversalSolution(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        node = root

        while node:
            if node.left:
                rightmost = node.left

                while rightmost.right:
                    rightmost = rightmost.right

                rightmost.right = node.right
                node.right = node.left
                node.left = None

            node = node.right

    def recursiveSolution(self, root: Optional[TreeNode]) -> None:
        def flattenTree(node):
            if not node:
                return None

            if not node.left and not node.right:
                return node

            left_tree_tail = flattenTree(node.left)
            right_tree_tail = flattenTree(node.right)

            if left_tree_tail:
                left_tree_tail.right = node.right
                node.right = node.left
                node.left = None

            return right_tree_tail if right_tree_tail else left_tree_tail

        flattenTree(root)
