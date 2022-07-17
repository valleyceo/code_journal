# LC 959. Regions Cut By Slashes

'''
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.
'''

# O(N*N*log(N)) time | O(N * N) space
#        |-> Inverse-Ackermann function a(N) more precisely
class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        xr = self.find(x)
        yr = self.find(y)
        self.root[xr] = yr

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        uf = UnionFind(4 * n * n)

        for i in range(n):
            for j in range(n):
                cell = 4 * (i * n + j)

                if grid[i][j] in "/ ":
                    uf.union(cell, cell + 1)
                    uf.union(cell + 2, cell + 3)

                if grid[i][j] in "\ ":
                    uf.union(cell, cell + 3)
                    uf.union(cell + 1, cell + 2)

                if i + 1 < n:
                    botcell = cell + 4 * n
                    uf.union(cell + 3, botcell + 1)

                if i - 1 >= 0:
                    topcell = cell - 4 * n
                    uf.union(cell + 1, topcell + 3)

                if j + 1 < n:
                    rightcell = cell + 4
                    uf.union(cell + 2, rightcell)

                if j - 1 >= 0:
                    leftcell = cell - 4
                    uf.union(cell, leftcell + 2)

        return sum(uf.find(x) == x for x in range(4 * n * n))
