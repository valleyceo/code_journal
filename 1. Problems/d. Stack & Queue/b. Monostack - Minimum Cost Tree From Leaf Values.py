# LC 1130. Minimum Cost Tree From Leaf Values

'''
Given an array arr of positive integers, consider all binary trees such that:

Each node has either 0 or 2 children;
The values of arr correspond to the values of each leaf in an in-order traversal of the tree.
The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree, respectively.
Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed this sum fits into a 32-bit integer.

A node is a leaf if and only if it has zero children.
'''
class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        return self.monostack(arr)

    # O(n^3) time | O(n^2) space
    def topdown(self, arr: List[int]) -> int:

        @lru_cache(None)
        def helper(l, r):
            if l >= r:
                return 0

            res = float('inf')

            for i in range(l, r):
                rootVal = max(arr[l:i+1]) * max(arr[i+1:r+1])
                res = min(res, rootVal + helper(l, i) + helper(i + 1, r))

            return res

        return helper(0, len(arr) - 1)

    # O(n^3) time | O(n^2) space
    def bottomup(self, arr: List[int]) -> int:
        n = len(arr)
        dp = [[float('inf') for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0

        for L in range(2, n + 1):
            for i in range(n - L + 1):
                j = i + L - 1

                for k in range(i, j):
                    root_val = max(arr[i:k+1]) * max(arr[k+1:j+1])
                    dp[i][j] = min(dp[i][j], root_val + dp[i][k] + dp[k+1][j])

        return dp[0][n-1]

    # O(n) time | O(n) space
    def monostack(self, arr: List[int]) -> int:
        stack = [float('inf')]
        res = 0

        for n in arr:
            while stack and stack[-1] <= n:
                curr = stack.pop()

                if stack:
                    res += curr * min(stack[-1], n)

            stack.append(n)

        while len(stack) > 2:
            res += stack.pop() * stack[-1]

        return res
