# LC 980. Unique Paths III

'''
You are given an m x n integer array grid where grid[i][j] could be:

1 representing the starting square. There is exactly one starting square.
2 representing the ending square. There is exactly one ending square.
0 representing empty squares we can walk over.
-1 representing obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        return self.dfsSolution(grid)

    def dfsSolution(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        start = []
        goal = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    count += 1

                if grid[i][j] == 1:
                    start = [i, j]

        visited = set()
        visited.add((start[0], start[1]))
        queue = [[start[0], start[1], visited]]
        count += 1
        res = 0

        while queue:
            r, c, seen = queue.pop()

            for r2, c2 in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= r2 < n and 0 <= c2 < m:
                    if grid[r2][c2] == 2 and len(seen) == count:
                        res += 1
                    elif grid[r2][c2] == 0 and (r2, c2) not in seen:
                        seen2 = seen.copy()
                        seen2.add((r2, c2))
                        queue.append([r2, c2, seen2])

        return res

    # O(3^N) time | O(N) space (recursion stack space)
    def backtrackSolution(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        count = 0
        start = []
        goal = []

        for i in range(n):
            for j in range(m):
                if grid[i][j] >= 0:
                    count += 1

                if grid[i][j] == 1:
                    start = [i, j]

        res = 0

        def backtrack(r, c, rem):
            nonlocal res

            if grid[r][c] == 2 and rem == 1:
                res += 1
                return

            temp = grid[r][c]
            grid[r][c] = -1

            for r2, c2 in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if 0 <= r2 < n and 0 <= c2 < m and grid >= 0:
                    backtrack(r2, c2, rem - 1)

            grid[r][c] = temp

        backtrack(start[0], start[1], count)
        return res
