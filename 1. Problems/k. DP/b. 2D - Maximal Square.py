# LC 221. Maximal Square

'''
Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
'''

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [0]*(n + 1)
        maxSquare = 0
        prev = 0
        
        for i in reversed(range(m)):
            for j in reversed(range(n)):
                temp = dp[j]
                
                if matrix[i][j] == "0":
                    dp[j] = 0
                else:
                    dp[j] = min(dp[j], prev, dp[j+1]) + 1
                
                prev = temp
                maxSquare = max(maxSquare, dp[j])
                
        return maxSquare * maxSquare