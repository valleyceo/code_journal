"""
Balanced Binary Tree

Solution
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""
# Optimal O(n) time, O(1) space, O(log(n)) stack

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        self.result = True
        self.checkBalanced(root, 0)
        
        return self.result
    
    def checkBalanced(self, root: TreeNode, depth: int) -> bool:
        if root is None or self.result == False:
            return depth
        
        l = self.checkBalanced(root.left, depth + 1)
        r = self.checkBalanced(root.right, depth + 1)
        
        if abs(l-r) > 1:
            self.result = False
        
        return max(l, r)