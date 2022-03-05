# LC 222. Count Complete Tree Nodes

'''
Given the root of a complete binary tree, return the number of the nodes in the tree.

According to Wikipedia, every level, except possibly the last, is completely filled in a complete binary tree, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

Design an algorithm that runs in less than O(n) time complexity.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        return self.binarySearchSolution(root)

    # O(n) time | O(log(n)) space
    def linearSolution(self, root) -> int:
        if root is None:
            return 0

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)

        return 1 + left + right

    # O(d^2) = O((logn)^2) time | O(1) space, double binary search
    def binarySearchSolution(self, root) -> int:
        def find_depth(n):
            d = 0
            while n.left:
                d += 1
                n = n.left

            return d

        def node_exist(idx, d, n) -> bool:
            left = 0
            right = 2**d - 1

            for _ in range(d):
                mid = (left + right ) // 2
                if mid < idx:
                    left = mid + 1
                    n = n.right
                else:
                    right = mid
                    n = n.left

            return n is not None

        if root is None:
            return 0

        depth = find_depth(root)

        if depth == 0:
            return 1

        left = 0
        right = 2**depth - 1

        while left <= right:
            mid = (left + right) // 2

            if node_exist(mid, depth, root):
                left = mid + 1
            else:
                right = mid - 1

        return (2**depth - 1) + left
