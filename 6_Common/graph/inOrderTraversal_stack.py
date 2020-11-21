# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        curr = root
        
        while True:
            
            if curr:
                stack.append(curr)
                curr = curr.left
            elif len(stack) > 0:
                curr = stack.pop()
                res += [curr.val]
                
                curr = curr.right
            else:
                break
                
        return res