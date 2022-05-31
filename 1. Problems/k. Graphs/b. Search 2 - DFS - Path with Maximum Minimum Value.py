# LC 1102. Path With Maximum Minimum Value

'''
Given an m x n integer matrix grid, return the maximum score of a path starting at (0, 0) and ending at (m - 1, n - 1) moving in the 4 cardinal directions.

The score of a path is the minimum value in that path.

For example, the score of the path 8 → 4 → 5 → 9 is 4.

Example 1:

Input: grid = [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
'''

class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        return self.bfsHeap(grid)

    # O(MNlog(MN)) time | O(MN) space
    def bfsHeap(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = [(-grid[0][0], 0, 0)]
        visited = set([(0, 0)])

        while queue:
            val, r, c = heapq.heappop(queue)

            if r == m-1 and c == n-1:
                return -val

            for r2, c2 in [[r+1, c], [r-1, c], [r, c-1], [r, c+1]]:
                if 0 <= r2 < m and 0 <= c2 < n and (r2, c2) not in visited:
                    visited.add((r2, c2))
                    heapq.heappush(queue, (max(val, -grid[r2][c2]), r2, c2))

        return -1

    # O(mnlog(k)) time | O(mn) space
    # k is min(first cell, last cell)
    def binarySearch(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def path_exist(score):
            visited = [[False] * n for _ in range(m)]
            visited[0][0] = True
            queue = [(0, 0)]

            while queue:
                r, c = queue.pop()

                if r == m-1 and c == n-1:
                    return True

                for r2, c2 in [[r+1, c], [r-1, c], [r, c-1], [r, c+1]]:
                    if 0 <= r2 < m and 0 <= c2 < n and not visited[r2][c2] and grid[r2][c2] >= score:
                        visited[r2][c2] = True
                        queue.append((r2, c2))

            return False

        low = 0
        high = min(grid[0][0], grid[-1][-1])

        while low < high:
            mid = (low + high + 1) // 2

            if path_exist(mid):
                low = mid
            else:
                high = mid - 1

        return low
