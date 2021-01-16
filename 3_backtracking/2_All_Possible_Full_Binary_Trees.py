"""
LC 894. All Possible Full Binary Trees

A full binary tree is a binary tree where each node has exactly 0 or 2 children.

Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.

Each node of each tree in the answer must have node.val = 0.

You may return the final list of trees in any order.

Example 1:

Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
Explanation:

1 <= N <= 20
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N % 2 == 0:
            return []
        
        self.cache = {}
        
        return self.backtrack(N)
    
    def backtrack(self, nodeLeft: int) -> List[TreeNode]:
        if nodeLeft == 1:
            return [TreeNode(0)]
        
        if nodeLeft in self.cache:
            return self.cache[nodeLeft]
        
        res = []
        for i in range(1, nodeLeft, 2):
            for left in self.backtrack(i):
                for right in self.backtrack(nodeLeft - i - 1):
                    tempNode = TreeNode(0)
                    tempNode.left = left
                    tempNode.right = right
                    res.append(tempNode)
        
        self.cache[nodeLeft] = res
        return res