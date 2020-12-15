"""
1504. Count Submatrices With All Ones

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
 

Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1
"""
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        dp = [[(0, 0) for i in range(len(mat[0]))] for j in range(len(mat))]
        res = 0
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if mat[r][c] == 1:
                    trow = 1
                    tcol = 1
                    
                    if r > 0:                    
                        trow = dp[r-1][c][0] + 1
                    
                    if c > 0:
                        tcol = dp[r][c-1][1] + 1
                        
                    dp[r][c] = (trow, tcol)
        
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                if dp[r][c] == (0,0):
                    continue
                    
                maxR = dp[r][c][0]
                
                for i in range(dp[r][c][1]):
                    maxR = min(maxR, dp[r][c-i][0])
                    res += maxR
                    
        return res