# LC 536. Construct Binary Tree from String

'''
You need to construct a binary tree from a string consisting of parenthesis and integers.

The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.

You always start to construct the left child node of the parent first if it exists.

Example 1:

Input: s = "4(2(3)(1))(6(5))"
Output: [4,2,6,3,1,5]

Example 2:

Input: s = "4(2(3)(1))(6(5)(7))"
Output: [4,2,6,3,1,5,7]

Example 3:

Input: s = "-4(2(3)(1))(6(5)(7))"
Output: [-4,2,6,3,1,5,7]
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        if s == "":
            return None

        def buildTree():
            nonlocal idx

            if s[idx] == ")":
                idx += 1
                return

            prev = idx
            while idx < len(s) and s[idx] not in "()":
                idx += 1

            node = TreeNode(s[prev:idx])

            if idx < len(s) and s[idx] == "(":
                idx += 1
                node.left = buildTree()

            if idx < len(s) and s[idx] == "(":
                idx += 1
                node.right = buildTree()

            idx += 1
            return node

        idx = 0
        return buildTree()
