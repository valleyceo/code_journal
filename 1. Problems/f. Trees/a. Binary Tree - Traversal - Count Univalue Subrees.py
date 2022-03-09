# LC 250. Count Univalue Subtrees

'''
Given the root of a binary tree, return the number of uni-value subtrees.

A uni-value subtree means all nodes of the subtree have the same value.

Example 1:

Input: root = [5,1,5,5,5,null,5]
Output: 4
Example 2:

Input: root = []
Output: 0
Example 3:

Input: root = [5,5,5,5,5,null,5]
Output: 6
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.isUni(root)
        return self.count

    def isUni(self, node) -> bool:
        if node is None:
            return True

        isUni = True
        isUni &= self.isUni(node.left) and not (node.left and node.val != node.left.val)
        isUni &= self.isUni(node.right) and not (node.right and node.val != node.right.val)

        if isUni:
            self.count += 1

        return isUni
