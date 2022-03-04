# LC 973. K Closest Points to Origin

'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
'''
class Data:
    def __init__(self, distance, point):
        self.distance = distance
        self.point = point

    def __lt__(self, other):
        return self.distance < other.distance

# O(nlogk) time | O(k) space
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heapArr = []

        for x, y in points:
            heapq.heappush(heapArr, Data(-self.distance(x, y), [x, y]))

            if len(heapArr) > K:
                heapq.heappop(heapArr)

        return [x.point for x in heapArr]

    def distance(self, x, y) -> int:
        return sqrt(x*x + y*y)
