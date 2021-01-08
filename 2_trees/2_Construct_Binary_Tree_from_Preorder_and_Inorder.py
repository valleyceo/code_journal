"""
Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""
# Optimal, O(n) time complexity, O(n) space complexity
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        hmap = {v: i for (i, v) in enumerate(inorder)}
        idx = 0
        
        def recursiveBuild(left: int, right: int) -> TreeNode:
            if left > right:
                return None
            
            nonlocal idx
            node = TreeNode(preorder[idx])
            nodeIdx = hmap[preorder[idx]]
            idx += 1
            
            node.left = recursiveBuild(left, nodeIdx - 1)
            node.right = recursiveBuild(nodeIdx + 1, right)
        
            return node
        
        return recursiveBuild(0, len(inorder) - 1)