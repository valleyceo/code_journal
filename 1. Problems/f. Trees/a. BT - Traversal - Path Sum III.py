# LC 437. Path Sum III

'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:

Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:

Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        return self.prefixSumSolution(root, targetSum)

    # O(n * log(n)) time | O(n * log(n))
    def naiveSolution(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, path):
            nonlocal res

            if node is None:
                return

            if node.val == targetSum:
                res += 1

            if targetSum - node.val in path:
                res += path[targetSum - node.val]

            new_path = defaultdict(int)
            new_path[node.val] += 1

            for v in path:
                new_path[v + node.val] += path[v]

            dfs(node.left, new_path)
            dfs(node.right, new_path)
            return

        path = defaultdict(int)
        res = 0
        dfs(root, path)

        return res

    # O(n) time | O(n) space
    def prefixSumSolution(self, root: Optional[TreeNode], targetSum: int) -> int:

        def dfs(node, path_sum):

            nonlocal res

            if node is None:
                return

            path_sum += node.val

            if path_sum == targetSum:
                res += 1

            res += prefix_sum_map[path_sum - targetSum]

            prefix_sum_map[path_sum] += 1

            dfs(node.left, path_sum)
            dfs(node.right, path_sum)

            prefix_sum_map[path_sum] -= 1


        res = 0
        prefix_sum_map = defaultdict(int)
        dfs(root, 0)

        return res
