"""
LC 85. Maximal Rectangle

Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example 1:

Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0

Constraints:

rows == matrix.length
cols == matrix.length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.
"""
# Time complexity: O(N^2), Space complexity: O(N)
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0
        
        arr = [0] * (len(matrix[0]) + 1)
        maxArea = 0
        
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == "1":
                    arr[c] += 1
                else:
                    arr[c] = 0
                    
            maxArea = self.findMaxRectangle(arr, maxArea)
            
        return maxArea
        
    def findMaxRectangle(self, heights: List[int], area: int) -> int:
        stack = [-1]
        
        for idx in range(len(heights)):
            while heights[idx] < heights[stack[-1]]:
                h = heights[stack.pop()]
                area = max(area, h * (idx - stack[-1] - 1))
            
            stack.append(idx)
        
        return area