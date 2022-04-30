# LC 987. Vertical Order Traversal of a Binary Tree

'''
Given the root of a binary tree, calculate the vertical order traversal of the binary tree.

For each node at position (row, col), its left and right children will be at positions (row + 1, col - 1) and (row + 1, col + 1) respectively. The root of the tree is at (0, 0).

The vertical order traversal of a binary tree is a list of top-to-bottom orderings for each column index starting from the leftmost column and ending on the rightmost column. There may be multiple nodes in the same row and same column. In such a case, sort these nodes by their values.

Return the vertical order traversal of the binary tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# O(n) time | O(n) space
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        mp = defaultdict(list)
        min_idx = 0
        max_idx = 0
        queue = [[root, 0]]

        while queue:
            temp = []
            temp_mp = defaultdict(list)

            for node, idx in queue:

                temp_mp[idx].append(node.val)

                if node.left:
                    temp.append([node.left, idx - 1])
                    min_idx = min(min_idx, idx - 1)

                if node.right:
                    temp.append([node.right, idx + 1])
                    max_idx = max(max_idx, idx + 1)

            for k, v in temp_mp.items():
                mp[k].extend(sorted(v))

            queue = temp

        res = []

        for i in range(min_idx, max_idx + 1):
            res.append(mp[i])

        return res
