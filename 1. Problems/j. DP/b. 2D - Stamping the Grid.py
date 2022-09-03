# LC 2132. Stamping the Grid

'''
You are given an m x n binary matrix grid where each cell is either 0 (empty) or 1 (occupied).

You are then given stamps of size stampHeight x stampWidth. We want to fit the stamps such that they follow the given restrictions and requirements:

Cover all the empty cells.
Do not cover any of the occupied cells.
We can put as many stamps as we want.
Stamps can overlap with each other.
Stamps are not allowed to be rotated.
Stamps must stay completely inside the grid.
Return true if it is possible to fit the stamps while following the given restrictions and requirements. Otherwise, return false.
'''

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        n = len(grid)
        m = len(grid[0])
        H, W = stampHeight, stampWidth

        def helper(M):
            dp = [[0] * (m + 1) for _ in range(n + 1)]

            for r, c in product(range(n), range(m)):
                dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1] - dp[r][c] + M[r][c]

            return dp

        def sumRegion(r1, c1, r2, c2):
            return dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1]

        dp = helper(grid)
        diff = [[0] * (m + 1) for _ in range(n + 1)]

        for r in range(n - H + 1):
            for c in range(m - W + 1):
                if sumRegion(r, c, r + H - 1, c + W - 1) == 0:
                    diff[r][c] += 1
                    diff[r][c+W] -= 1
                    diff[r+H][c] -= 1
                    diff[r+H][c+W] += 1

        dp2 = helper(diff)

        for r, c in product(range(n), range(m)):
            if dp2[r + 1][c + 1] == 0 and grid[r][c] != 1:
                return False

        return True

"""
Source: https://leetcode.com/problems/stamping-the-grid/discuss/1675344/Python-2d-cumulative-sums-explained
"""
