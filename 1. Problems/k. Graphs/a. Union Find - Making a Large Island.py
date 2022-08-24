# 827. Making A Large Island

'''
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.
'''
# O(N^2) time | O(N^2) space
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def find(x, root):
            if not x == root[x]:
                root[x] = find(root[x], root)

            return root[x]

        def union(x, y, root):
            rx = find(x, root)
            ry = find(y, root)

            if rx != ry:
                root[ry] = rx

        n = len(grid)
        uf_root = [i for i in range(n * n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    continue

                for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if not (0 <= i2 < n) or not (0 <= j2 < n):
                        continue

                    if grid[i2][j2] == 0:
                        continue

                    id1 = i * n + j
                    id2 = i2 * n + j2

                    union(id1, id2, uf_root)

        id_counts = defaultdict(int)
        res = 0

        for i in range(n * n):
            rid = find(i, uf_root)
            id_counts[rid] += 1
            res = max(res, id_counts[rid])

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    continue

                neighbors = set()

                for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if not (0 <= i2 < n) or not (0 <= j2 < n):
                        continue

                    if grid[i2][j2] == 0:
                        continue

                    id2 = i2 * n + j2
                    neighbors.add(find(id2, uf_root))

                count = 1

                for rid in neighbors:
                    count += id_counts[rid]

                res = max(res, count)

        return res
