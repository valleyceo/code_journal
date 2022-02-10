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
# Time complexity: O(NM), Space complexity: O(N)
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if len(mat) == 0 or len(mat[0]) == 0:
            return 0
        
        R = len(mat)
        C = len(mat[0])
        arr = [0] * (C + 1)
        res = 0
        
        for r in range(R):
            dp = [0] * (C + 1)
            stack = [-1]
            for c in range(C):
                
                if mat[r][c] == 1:
                    arr[c] += 1
                else:
                    arr[c] = 0
                
                while arr[c] < arr[stack[-1]]:
                    stack.pop()
                
                dp[c] = dp[stack[-1]] + arr[c]*(c-stack[-1])
                stack.append(c)
                
            res += sum(dp)
        
        return res