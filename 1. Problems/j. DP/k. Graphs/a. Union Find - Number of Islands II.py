# LC 305. Number of Islands II

'''
You are given an empty 2D binary grid grid of size m x n. The grid represents a map where 0's represent water and 1's represent land. Initially, all the cells of grid are water cells (i.e., all the cells are 0's).

We may perform an add land operation which turns the water at position into a land. You are given an array positions where positions[i] = [ri, ci] is the position (ri, ci) at which we should operate the ith operation.

Return an array of integers answer where answer[i] is the number of islands after turning the cell (ri, ci) into a land.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''
# O(mn + L) time, L is the number of operations | O(mn) space
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(x):
            while x in parents:
                if parents[x] in parents:
                    parents[x] = parents[parents[x]]
                x = parents[x]

            return x

        def union(x, y):
            p_x = find(x)
            p_y = find(y)

            if p_x == p_y:
                return False

            parents[p_x] = p_y
            return True

        visited = set()
        parents = {}
        res = []
        count = 0

        for x, y in positions:

            if (x, y) not in visited:
                visited.add((x, y))
                count += 1

                for i, j in [[x+1, y], [x-1, y], [x, y+1], [x, y-1]]:
                    if (i, j) in visited and union((i, j), (x, y)):
                        count -= 1

            res.append(count)

        return res
