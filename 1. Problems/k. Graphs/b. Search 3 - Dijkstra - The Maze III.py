# LC 499. The Maze III

'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction. There is also a hole in this maze. The ball will drop into the hole if it rolls onto the hole.

Given the m x n maze, the ball's position ball and the hole's position hole, where ball = [ballrow, ballcol] and hole = [holerow, holecol], return a string instructions of all the instructions that the ball should follow to drop in the hole with the shortest distance possible. If there are multiple valid instructions, return the lexicographically minimum one. If the ball can't drop in the hole, return "impossible".

If there is a way for the ball to drop in the hole, the answer instructions should contain the characters 'u' (i.e., up), 'd' (i.e., down), 'l' (i.e., left), and 'r' (i.e., right).

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).
'''

class Solution:
    def findShortestWay(self, maze: List[List[int]], ball: List[int], hole: List[int]) -> str:
        m = len(maze)
        n = len(maze[0])
        dest = tuple(hole)
        queue = [[0, tuple(ball), ""]]
        min_dist = float('inf')
        res = []
        visited = set()

        while queue:
            dist, pos, pstr = heapq.heappop(queue)

            if pos in visited:
                continue

            if pos == dest:
                return pstr

            visited.add(pos)

            for dchr, di, dj in [["u", -1, 0], ["r", 0, 1], ["l", 0, -1], ["d", 1, 0]]:
                i, j = pos
                steps = 0

                while 0 <= i + di < m and 0 <= j + dj < n and maze[i + di][j + dj] == 0:
                    i += di
                    j += dj
                    steps += 1

                    if (i, j) == dest:
                        break

                heapq.heappush(queue, [dist + steps, (i, j), pstr + dchr])

        return "impossible"
