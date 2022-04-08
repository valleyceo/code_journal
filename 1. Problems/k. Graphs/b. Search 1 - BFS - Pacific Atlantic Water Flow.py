# LC 417. Pacific Atlantic Water Flow

'''
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
'''

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n = len(heights)
        m = len(heights[0])
        neighbors = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def is_valid(i, j):
            return 0 <= i < n and 0 <= j < m

        def dfs(i, j, visited):
            if (i, j) in visited:
                return

            visited.add((i, j))

            for d in neighbors:
                i2 = i + d[0]
                j2 = j + d[1]

                if not is_valid(i2, j2):
                    continue

                if heights[i2][j2] < heights[i][j]:
                    continue

                dfs(i2, j2, visited)

        atlantic = set()
        pacific = set()

        for i in range(n):
            dfs(i, 0, pacific)
            dfs(i, m - 1, atlantic)

        for j in range(m):
            dfs(0, j, pacific)
            dfs(n - 1, j, atlantic)

        return atlantic.intersection(pacific)
