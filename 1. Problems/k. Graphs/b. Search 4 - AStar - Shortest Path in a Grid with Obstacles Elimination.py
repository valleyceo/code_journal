# LC 1293. Shortest Path in a Grid with Obstacles Elimination

'''
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        return self.aStarSolution(grid, k)

    # BFS O(NK) time | O(NK) space
    # N is number of cells, K is max obstacle skips
    def bfsSolution(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])

        if k >= m + n - 2:
            return m + n - 2

        state = (0, 0, k)
        queue = deque([(state, 0)])
        visited = set([state])
        target = (m - 1, n - 1)

        while queue:
            (r, c, skip), steps = queue.popleft()

            if (r, c) == target:
                return steps

            for r2, c2 in [[r, c+1], [r, c-1], [r+1,c], [r-1,c]]:
                if (0 <= r2 < m) and (0 <= c2 < n):
                    skip2 = skip - 1 if grid[r2][c2] else skip

                    state2 = (r2, c2, skip2)

                    if skip2 >= 0 and state2 not in visited:
                        visited.add(state2)
                        queue.append((state2, steps + 1))

        return -1

    # A* O(NKlog(NK)) time | O(NK) space
    # N is number of cells, K is max obstacle skips
    def aStarSolution(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        target = (m - 1, n - 1)

        def getDistance(row, col):
            return target[0] - row + target[1] - col

        state = (0, 0, k)
        # Note the order is important when using priority queue -> est_path_dist, steps, state
        queue = [(getDistance(0, 0), 0, state)]
        visited = set([state])

        while queue:
            est_path_dist, steps, (r, c, rem_skip) = heapq.heappop(queue)
            rem_dist = est_path_dist - steps

            if rem_dist <= rem_skip:
                return est_path_dist

            for r2, c2 in [[r, c+1], [r, c-1], [r+1,c], [r-1,c]]:
                if (0 <= r2 < m) and (0 <= c2 < n):
                    rem_skip2 = rem_skip - 1 if grid[r2][c2] else rem_skip
                    state2 = (r2, c2, rem_skip2)

                    if rem_skip2 >= 0 and state2 not in visited:
                        visited.add(state2)
                        est_path_dist2 = getDistance(r2, c2) + steps + 1
                        heapq.heappush(queue, (est_path_dist2, steps + 1, state2))

        return -1
