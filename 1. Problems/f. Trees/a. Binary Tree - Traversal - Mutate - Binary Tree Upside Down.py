# LC 156. Binary Tree Upside Down

'''
Given the root of a binary tree, turn the tree upside down and return the new root.

You can turn a binary tree upside down with the following steps:

The original left child becomes the new root.
The original root becomes the new right child.
The original right child becomes the new left child.

The mentioned steps are done level by level. It is guaranteed that every right node has a sibling (a left node with the same parent) and has no children.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def traverse(node):
            if not node or (node.left is None and node.right is None):
                return node

            left = traverse(node.left)

            node.left.left = node.right
            node.left.right = node
            node.right = None
            node.left = None

            return left

        return traverse(root)
