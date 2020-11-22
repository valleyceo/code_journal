"""
LC 119 Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]
 

Constraints:

0 <= rowIndex <= 40
"""
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        self.dp = {}
        self.res = [1] * (rowIndex + 1)
        
        for i in range(0, rowIndex+1):
            self.res[i] = self.getCell(rowIndex, i)
        
        return self.res
    
    def getCell(self, r: int, c: int) -> int:
        if c == 0 or c == r:
            return 1
        
        minc = min(c, r - c)
        if (r, minc) not in self.dp:
            self.dp[(r, minc)] = self.getCell(r-1, c) + self.getCell(r-1, c-1)
        
        return self.dp[(r, minc)]