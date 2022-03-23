# LC 99. Recover Binary Search Tree

'''
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.morrisSolution(root)

    # O(n) time | O(1) space
    def morrisSolution(self, root: Optional[TreeNode]) -> None:
        curr = root
        x = y = None
        pred = None

        while curr:
            if curr.left is None:

                if pred and pred.val > curr.val:

                    y = curr

                    if x is None:
                        x = pred

                pred = curr
                curr = curr.right
            else:
                prev = curr.left

                while prev.right and prev.right != curr:
                    prev = prev.right

                if prev.right is None:
                    prev.right = curr
                    curr = curr.left
                else:
                    prev.right = None

                    if pred and pred.val > curr.val:
                        y = curr

                        if x is None:
                            x = pred

                    pred = curr
                    curr = curr.right

        x.val, y.val = y.val, x.val

    def iterativeSolution(self, root: Optional[TreeNode]) -> None:
        stack = []
        x = y = None
        pred = None
        curr = root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()

            if pred and pred.val > curr.val:
                y = curr

                if x is None:
                    x = pred
                else:
                    break

            pred = curr
            curr = curr.right

        x.val, y.val = y.val, x.val

    def recursiveSolution(self, root: Optional[TreeNode]) -> None:

        def traverse(node):
            nonlocal pred, x, y

            if node is None:
                return

            traverse(node.left)

            if pred and pred.val > node.val:
                y = node

                if x is None:
                    x = pred
                else:
                    return

            pred = node
            traverse(node.right)

        x = y = None
        pred = None
        traverse(root)
        x.val, y.val = y.val, x.val


    def understandableSolution(self, root: Optional[TreeNode]) -> None:

        # convert to list
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        # swap two misplaced
        def find_two_misplaced(nums):
            n = len(nums)
            x = y = None

            for i in range(n - 1):
                if nums[i + 1] < nums[i]:
                    y = nums[i + 1]

                    if x is None:
                        x = nums[i]
                    else:
                        break

            return x, y

        # recover two misplaced in tree
        def recover(root, fix_count):
            if root is None:
                return

            if root.val == x or root.val == y:
                root.val = y if root.val == x else x
                fix_count -= 1

                if fix_count == 0:
                    return

            recover(root.left, fix_count)
            recover(root.right, fix_count)

        arr = inorder(root)
        x, y = find_two_misplaced(arr)
        recover(root, 2)
