"""
LC 95 Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
 

Constraints:

0 <= n <= 8
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        
        arr = [i+1 for i in range(n)]
        return self.recurse(arr)
        
    def recurse(self, arr: List[int]) -> List[TreeNode]:
        if len(arr) == 0:
            return [None]
        elif len(arr) == 1:
            return [TreeNode(arr[0])]
            
        perm = []
        
        for i in range(len(arr)):
            for l in self.recurse(arr[:i]):
                for r in self.recurse(arr[i+1:]):
                    perm.append(TreeNode(arr[i], l, r))
        
        return perm or [None]