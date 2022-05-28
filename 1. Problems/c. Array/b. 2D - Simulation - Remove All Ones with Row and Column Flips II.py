# LC 2174. Remove All Ones With Row and Column Flips II

'''
You are given a 0-indexed m x n binary matrix grid.

In one operation, you can choose any i and j that meet the following conditions:

0 <= i < m
0 <= j < n
grid[i][j] == 1
and change the values of all cells in row i and column j to zero.

Return the minimum number of operations needed to remove all 1's from grid.
'''
# Backtrack solution
class Solution:
    def removeOnes(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        res = float('inf')

        def backtrack(flips):
            nonlocal res

            flag = False

            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1 and ('r', i) not in visited and ('c', j) not in visited:

                        flag = True

                        visited.add(('r', i))
                        visited.add(('c', j))

                        backtrack(flips + 1)

                        visited.remove(('r', i))
                        visited.remove(('c', j))

            if not flag:
                res = min(res, flips)

        backtrack(0)
        return res
