"""
LC 106. Construct Binary Tree from Inorder and Postorder Traversal

Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# O(n) time complexity, O(n) space complexity
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        hmap = {v: i for (i, v) in enumerate(inorder)}
        
        def recursiveBuild(left:int, right: int):
            if left > right:
                return None
            
            node = TreeNode(postorder.pop())
            idx = hmap[node.val]
            node.right = recursiveBuild(idx+1, right)
            node.left = recursiveBuild(left, idx-1)
            return node
            
        return recursiveBuild(0, len(postorder)-1)