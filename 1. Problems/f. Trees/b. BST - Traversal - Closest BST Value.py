# 270. Closest Binary Search Tree Value

'''
Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target.

Example 1:

Input: root = [4,2,5,1,3], target = 3.714286
Output: 4
Example 2:

Input: root = [1], target = 4.428571
Output: 1

Constraints:

The number of nodes in the tree is in the range [1, 104].
0 <= Node.val <= 10^9
-109 <= target <= 10^9
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        return self.iterative(root, target)

    def iterative(self, node, target) -> int:
        closest = node.val

        while node:
            if abs(node.val - target) < abs(closest - target):
                closest = node.val

            if node.val >= target:
                node = node.left
            else:
                node = node.right

        return closest

    def recursive(self, node, target) -> int:
        if node is None:
            return None

        closest = None

        if node.val >= target:
            closest = self.recursive(node.left, target)
        else:
            closest = self.recursive(node.right, target)

        if closest != None and abs(target - node.val) > abs(target - closest):
            return closest
        else:
            return node.val
