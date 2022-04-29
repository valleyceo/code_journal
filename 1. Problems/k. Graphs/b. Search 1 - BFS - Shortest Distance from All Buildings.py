# LC 317. Shortest Distance from All Buildings

'''
You are given an m x n grid grid of values 0, 1, or 2, where:
- each 0 marks an empty land that you can pass by freely,
- each 1 marks a building that you cannot pass through, and
- each 2 marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        return self.solution1(grid)

    # O(N^2M^2) time | O(NM) space
    def naiveTLE(self, grid: List[List[int]]) -> int:
        def isValid(i, j):
            nonlocal n, m

            return 0 <= i < n and 0 <= j < m

        def dfs(i, j, count):

            queue = deque([[i, j, 0]])
            visited = set([(i, j)])
            total_dist = 0
            total_count = 0

            while queue:
                r, c, dist = queue.popleft()

                if grid[r][c] == 1:
                    total_dist += dist
                    total_count += 1
                    continue

                for r2, c2 in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                    if not isValid(r2, c2) or (r2, c2) in visited:
                        continue

                    if grid[r2][c2] == 2:
                        continue

                    visited.add((r2, c2))
                    queue.append([r2, c2, dist + 1])

            return total_dist if total_count == count else -1

        n = len(grid)
        m = len(grid[0])
        res = float('inf')
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    dist = dfs(i, j, count)

                    if dist != -1:
                        res = min(res, dist)

        return res if res != float('inf') else -1

    # Building to Land computation (DP)
    # O(N^2M^2) time | O(NM) space
    def solution1(self, grid: List[List[int]]) -> int:
        def isValid(i, j):
            nonlocal n, m
            return 0 <= i < n and 0 <= j < m

        def find_shortest_distances(bi, bj, lands):

            queue = deque([[bi, bj, 0]])
            visited = set()

            while queue:
                r, c, dist = queue.popleft()

                if (r, c) in lands:
                    lands[(r, c)] += dist

                for r2, c2 in [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]:
                    if not isValid(r2, c2) or (r2, c2) in visited:
                        continue

                    if (r2, c2) not in lands:
                        continue

                    visited.add((r2, c2))
                    queue.append([r2, c2, dist + 1])

            if len(visited) != len(lands):
                for position in set(lands.keys()).difference(visited):
                    lands.pop(position)

            return

        n = len(grid)
        m = len(grid[0])
        res = float('inf')
        count = 0
        buildings = []
        lands = {}

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    buildings.append((i, j))

                if grid[i][j] == 0:
                    lands[(i, j)] = 0

        for r, c in buildings:
            find_shortest_distances(r, c, lands)

        for v in lands.values():
            if v == 0:
                return -1

        return min(lands.values()) if buildings and lands else -1

"""
Insight:
- Instead of computing dist from every land to buildings, compute dist from each building to all lands
"""
