# LC 2258. Escape the Spreading Fire

'''
You are given a 0-indexed 2D integer array grid of size m x n which represents a field. Each cell has one of three values:

0 represents grass,
1 represents fire,
2 represents a wall that you and fire cannot pass through.
You are situated in the top-left cell, (0, 0), and you want to travel to the safehouse at the bottom-right cell, (m - 1, n - 1). Every minute, you may move to an adjacent grass cell. After your move, every fire cell will spread to all adjacent cells that are not walls.

Return the maximum number of minutes that you can stay in your initial position before moving while still safely reaching the safehouse. If this is impossible, return -1. If you can always reach the safehouse regardless of the minutes stayed, return 109.

Note that even if the fire spreads to the safehouse immediately after you have reached it, it will be counted as safely reaching the safehouse.

A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).
'''

class Solution:
    def maximumMinutes(self, grid: List[List[int]]) -> int:
        return self.binarySearch(grid)

    def binarySearch(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        inf = 10 ** 10

        def isvalid(r, c):
            return 0 <= r < m and 0 <= c < n

        fires = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fires.append([i, j, 0])

        for i in range(m):
            for j in range(n):
                grid[i][j] = inf if grid[i][j] < 2 else -1

        def bfs(queue, seen):
            for i, j, time in queue:
                if seen[i][j] < inf:
                    continue

                seen[i][j] = time

                for i2, j2 in [[i, j+1], [i, j-1], [i-1, j], [i+1, j]]:
                    if isvalid(i2, j2) and seen[i2][j2] >= inf and time + 1 < grid[i2][j2]:
                        queue.append([i2, j2, time + 1])

        def isdead(time):
            seen = [[inf + 10] * n for i in range(m)]
            bfs([[0, 0, time]], seen)
            return seen[-1][-1] > grid[-1][-1]

        bfs(fires, grid)
        grid[-1][-1] += 1
        return bisect_left(range(10**9 + 1), True, key = isdead) - 1
