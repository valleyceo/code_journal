"""
LC 1411. Number of Ways to Paint N × 3 Grid

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colours: Red, Yellow or Green while making sure that no two adjacent cells have the same colour (i.e no two cells that share vertical or horizontal sides have the same colour).

You are given n the number of rows of the grid.

Return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 10^9 + 7.

Example 1:

Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown:

Example 2:

Input: n = 2
Output: 54
Example 3:

Input: n = 3
Output: 246
Example 4:

Input: n = 7
Output: 106494
Example 5:

Input: n = 5000
Output: 30228214

Constraints:

n == grid.length
grid[i].length == 3
1 <= n <= 5000
"""
# Time complexity: O(12N), space complexity: O(12N)
class Solution:
    def numOfWays(self, n: int) -> int:
        self.n = n
        self.cache = {}
        
        res = 0
        for v1 in range(3):
            for v2 in range(3):
                for v3 in range(3):
                    res += self.backtrack(0, v1, v2, v3, -1, -1, -1)
        
        return res % (10**9 + 7)
        
    def backtrack(self, r, c1, c2, c3, p1, p2, p3) -> int:
        if c1 == c2 or c2 == c3:
            return 0
        
        if c1 == p1 or c2 == p2 or c3 == p3:
            return 0
        
        if r == self.n-1:
            return 1
        
        if (r, c1, c2, c3) in self.cache:
            return self.cache[(r, c1, c2, c3)]
        
        pathSum = 0
        for v1 in range(3):
            for v2 in range(3):
                for v3 in range(3):
                    pathSum += self.backtrack(r + 1, v1, v2, v3, c1, c2, c3)
                    pathSum %= (10**9 + 7)
                    
        self.cache[(r, c1, c2, c3)] = pathSum % (10**9 + 7)
        return pathSum % (10**9 + 7)