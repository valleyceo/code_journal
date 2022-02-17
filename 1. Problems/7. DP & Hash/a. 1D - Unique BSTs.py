# LC 96. Unique Binary Search Trees

'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:

Input: n = 3
Output: 5
Example 2:

Input: n = 1
Output: 1

Constraints:
1 <= n <= 19
'''
class Solution:
    def numTrees(self, n: int) -> int:
        return self.bottomUp(n)

    # O(N^2) time, O(N) space
    @lru_cache(None)
    def topDown(self, n: int) -> int:
        if n <= 2:
            return n

        total = 0

        for i in range(n):
            total += self.numTrees(max(1, i)) * self.numTrees(max(1, n - i - 1))

        return total

    # O(N^2) time, O(N) space
    def bottomUp(self, n: int) -> int:
        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j-1] * G[i-j]

        return G[n]

    # O(N) time, O(1) space
    def catalan(self, n: int) -> int:
        C = 1

        for i in range(n):
            C = C * 2 * (2 * i + 1) / (i + 2)

        return int(C)
