# LC 562. Longest Line of Consecutive One in Matrix

'''
Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.

The line could be horizontal, vertical, diagonal, or anti-diagonal.
'''
# O(MN) time | O(4N) space
# M is row, N is column
class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        R = len(mat)
        C = len(mat[0])

        # [top, left, top_left, top_right]
        dp = [[0]*4 for _ in range(C)]
        res = 0

        for i in range(R):
            old = 0

            for j in range(C):
                if mat[i][j] == 1:
                    # top
                    dp[j][0] = dp[j][0] + 1 if (i > 0) else 1

                    # left
                    dp[j][1] = dp[j-1][1] + 1 if (j > 0) else 1

                    # top_left
                    temp = dp[j][2]
                    dp[j][2] = old + 1 if (i > 0 and j > 0) else 1
                    old = temp

                    # top_right
                    dp[j][3] = dp[j+1][3] + 1 if (i > 0 and j < C - 1) else 1

                else:
                    old = dp[j][2]
                    dp[j] = [0,0,0,0]

                res = max(res, max(dp[j]))

        return res
