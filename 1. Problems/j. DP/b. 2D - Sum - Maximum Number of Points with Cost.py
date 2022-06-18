# LC 1937. Maximum Number of Points with Cost

'''
You are given an m x n integer matrix points (0-indexed). Starting with 0 points, you want to maximize the number of points you can get from the matrix.

To gain points, you must pick one cell in each row. Picking the cell at coordinates (r, c) will add points[r][c] to your score.

However, you will lose points if you pick a cell too far from the cell that you picked in the previous row. For every two adjacent rows r and r + 1 (where 0 <= r < m - 1), picking cells at coordinates (r, c1) and (r + 1, c2) will subtract abs(c1 - c2) from your score.

Return the maximum number of points you can achieve.

abs(x) is defined as:

x for x >= 0.
-x for x < 0.
'''
# O(MN) time | O(1) if using input, O(n) if using row
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        m = len(points)
        n = len(points[0])

        for i in range(m - 1):
            for j in range(n - 2, -1, -1):
                points[i][j] = max(points[i][j], points[i][j + 1] - 1)

            for j in range(1, n):
                points[i][j] = max(points[i][j], points[i][j - 1] - 1)

            for j in range(n):
                points[i + 1][j] += points[i][j]

        return max(points[-1])

"""
Insight:
- The max of prev column is independent to current row
    -> Process maxval for each column separately, then add it to next row
"""
