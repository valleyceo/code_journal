# LC 447. Number of Boomerangs

'''
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2

Example 3:

Input: points = [[1,1]]
Output: 0
'''

# O(N^2) time | O(N) space
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:

        res = 0

        for i in range(len(points)):

            dist_map = defaultdict(int)

            for j in range(len(points)):
                y = points[i][0] - points[j][0]
                x = points[i][1] - points[j][1]
                dist = x*x + y*y

                dist_map[dist] += 1

            for k, v in dist_map.items():
                res += v * (v - 1)

        return res

"""
NOTE:
- Note that you are finding 3 points -> 2 Points that are in same distance from ONE STARTING point
- From every point, get distance of other points, save counts in hashmap
- If there are x values in distance of a point, possible combinations are x * (x - 1)
"""
