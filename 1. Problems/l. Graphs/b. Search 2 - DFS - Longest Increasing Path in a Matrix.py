# 329. Longest Increasing Path in a Matrix

'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 200
0 <= matrix[i][j] <= 231 - 1
'''
# O(mn) time | O(mn) space
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        self.M = matrix
        self.rlen = len(matrix)
        self.clen = len(matrix[0])
        self.dir = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        self.dp = [[-1 for x in range(self.clen)] for y in range(self.rlen)]
        res = 0

        for i in range(self.rlen):
            for j in range(self.clen):
                val = self.search(i, j)
                res = max(res, val)
        return res

    def search(self, r: int, c: int) -> int:

        maxLen = 0
        if self.dp[r][c] >= 0:
            return self.dp[r][c]

        for dr, dc in self.dir:
            r2 = dr + r
            c2 = dc + c

            if r2 < 0 or r2 >= self.rlen or c2 < 0 or c2 >= self.clen:
                continue

            if self.M[r][c] < self.M[r2][c2]:
                maxLen = max(maxLen, self.search(r2, c2))

        self.dp[r][c] = maxLen + 1
        return maxLen + 1
