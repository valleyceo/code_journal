"""
LC 450 Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.
* Follow up: Can you solve it with time complexity O(height of tree)?

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
        
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        
        pre = None
        node = root
        
        while node is not None:
            if node.val == key:
                break
            
            pre = node
            if key < node.val:
                node = node.left
            else:
                node = node.right
        
        if node is None:
            return root
        
        if pre is None:
            root = self.delNode(node)
            return root
        
        if pre.left is node:
            pre.left = self.delNode(node)
        else:
            pre.right = self.delNode(node)
        
        return root
    
    def delNode(self, node: TreeNode) -> TreeNode:
        if node.left is None and node.right is None:
            return None
    
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        
        pre = node
        curr = node.right
        
        while curr.left is not None:
            pre = curr
            curr = curr.left
        
        node.val = curr.val
        
        if pre.left == curr:
            pre.left = curr.right
        else:
            pre.right = curr.right
        
        return node