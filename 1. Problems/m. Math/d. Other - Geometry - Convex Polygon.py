# LC 469. Convex Polygon

'''
You are given an array of points on the X-Y plane points where points[i] = [xi, yi]. The points form a polygon when joined sequentially.

Return true if this polygon is convex and false otherwise.

You may assume the polygon formed by given points is always a simple polygon. In other words, we ensure that exactly two edges intersect at each vertex and that edges otherwise don't intersect each other.
'''
class Solution:
    def isConvex(self, points: List[List[int]]) -> bool:
        def direction(X, Y, Z):
            return (Y[0] - X[0]) * (Z[1] - X[1]) - (Y[1] - X[1]) * (Z[0] - X[0])

        d = None

        for i in range(len(points)):
            d_next = direction(points[i-2], points[i-1], points[i])

            if d_next == 0:
                continue

            if d == None:
                d = d_next
            elif d * d_next < 0:
                return False

        return True
