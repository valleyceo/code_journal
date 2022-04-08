# 124. Binary Tree Maximum Path Sum

'''
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        :type root: TreeNode
        :rtype: int
        """

        def traverse(node):
            nonlocal max_sum
            if node is None:
                return 0

            left = max(traverse(node.left), 0)
            right = max(traverse(node.right), 0)
            max_sum = max(max_sum, left + right + node.val)

            return node.val + max(left, right)

        max_sum = float('-inf')
        traverse(root)
        return max_sum
