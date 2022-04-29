# LC 296. Best Meeting Point

'''
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
'''

class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        return self.unsortedSolution(grid)

    # O(MNLog(MN)) time | O(MN) space
    def sortSolution(self, grid: List[List[int]]) -> int:
        def getDist(points, mid):
            dist = 0

            for p in points:
                dist += abs(p - mid)

            return dist

        rows = []
        cols = []
        ct = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)
                    cols.append(j)

        cols.sort()
        rmid = rows[len(rows) // 2]
        cmid = cols[len(cols) // 2]

        return getDist(rows, rmid) + getDist(cols, cmid)

    # O(MN) time | O(MN) space
    def unsortedSolution(self, grid: List[List[int]]) -> int:
        def getDist(points):
            dist = 0
            left = 0
            right = len(points) - 1

            while left < right:
                dist += points[right] - points[left]
                left += 1
                right -= 1

            return dist

        rows = []
        cols = []

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    rows.append(i)

        for i in range(len(grid[0])):
            for j in range(len(grid)):
                if grid[j][i] == 1:
                    cols.append(i)

        return getDist(rows) + getDist(cols)
"""
Note:
 - As long as there are equal number of points on both sides, total distance is minimized
 - You can separate problem horizontally and vertically
"""
