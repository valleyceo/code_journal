# LC 1240. Tiling a Rectangle with the Fewest Squares

'''
Given a rectangle of size n x m, return the minimum number of integer-sided squares that tile the rectangle.
'''

class Solution:
    def tilingRectangle(self, n: int, m: int) -> int:

        def backtrack(cols, moves):
            nonlocal res

            if all(c == n for c in cols):
                res = min(res, moves)
                return

            if moves > res:
                return

            min_col = min(cols)
            min_idx = cols.index(min_col)

            idx = min_idx + 1

            while idx < m and cols[idx] == min_col:
                idx += 1

            for i in range(min(idx - min_idx, n - min_col), 0, -1):
                next_cols = cols[:]

                for j in range(i):
                    next_cols[min_idx + j] += i

                backtrack(next_cols, moves + 1)

        res = n * m
        backtrack([0] * m, 0)
        return res

"""
Note:
- Source: https://leetcode.com/problems/tiling-a-rectangle-with-the-fewest-squares/discuss/414716/Python-two-solutions%3A-backtracking-and-A*-search
"""
