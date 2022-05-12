# LC 407. Trapping Rain Water II

'''
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.

Example 1:

Input: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
Output: 4
Explanation: After the rain, water is trapped between the blocks.
We have two small ponds 1 and 3 units trapped.
The total volume of water trapped is 4.
'''
# O(MNlog(MN)) time | O(MN) space
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        visited = set()
        res = 0

        for i in range(m):
            for j in range(n):
                if i in {0, m - 1} or j in {0, n - 1}:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited.add((i, j))

        while heap:
            h, i, j = heapq.heappop(heap)

            for i2, j2 in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 < i2 < m - 1 and 0 < j2 < n - 1 and (i2, j2) not in visited:
                    res += max(h - heightMap[i2][j2], 0)
                    heapq.heappush(heap, (max(heightMap[i2][j2], h), i2, j2))
                    visited.add((i2, j2))

        return res

"""
# Insight:
- Start from the boundary, search inner cells
- Using priority queue (lowest column) guarantees that any cells lower than that creates a water trap by the difference amount
"""
