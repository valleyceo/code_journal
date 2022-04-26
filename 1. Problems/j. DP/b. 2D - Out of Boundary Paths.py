# LC 576. Out of Boundary Paths

'''
There is an m x n grid with a ball. The ball is initially at the position [startRow, startColumn]. You are allowed to move the ball to one of the four adjacent cells in the grid (possibly out of the grid crossing the grid boundary). You can apply at most maxMove moves to the ball.

Given the five integers m, n, maxMove, startRow, startColumn, return the number of paths to move the ball out of the grid boundary. Since the answer can be very large, return it modulo 10^9 + 7.
'''

class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        return self.topDown(m, n, maxMove, startRow, startColumn)

    def bruteForceDFS(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        def isInside(r, c):
            return 0 <= r < m and 0 <= c < n

        queue = [[0, [startRow, startColumn]]]
        res = 0

        while queue:

            dist, pos = queue.pop()

            if dist == maxMove:
                continue

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                r = pos[0] + dr
                c = pos[1] + dc

                if not isInside(r, c):
                    res += 1
                    continue

                queue.append([dist + 1, [r, c]])

        return res

    # Top Down DP solution
    # O(N*n*m) time | O(N*n*m) space
    def topDown(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:

        mod = 10**9 + 7

        @lru_cache(None)
        def dfs(N, i, j):
            if i == m or j == n or i < 0 or j < 0:
                return 1

            if N == 0:
                return 0

            return (dfs(N - 1, i + 1, j) + dfs(N - 1, i - 1, j) + dfs(N - 1, i, j + 1) + dfs(N - 1, i, j - 1)) % mod


        return dfs(maxMove, startRow, startColumn) % mod
