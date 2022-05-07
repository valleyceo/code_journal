# LC 505. The Maze II

'''
There is a ball in a maze with empty spaces (represented as 0) and walls (represented as 1). The ball can go through the empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

Given the m x n maze, the ball's start position and the destination, where start = [startrow, startcol] and destination = [destinationrow, destinationcol], return the shortest distance for the ball to stop at the destination. If the ball cannot stop at destination, return -1.

The distance is the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included).

You may assume that the borders of the maze are all walls (see examples).
'''
class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        def isValid(row, col):
            return 0 <= row < len(maze) and 0 <= col < len(maze[0])

        queue = [[0, start[0], start[1]]]
        visited = {tuple(start): 0}

        while queue:
            dist, r, c = heapq.heappop(queue)

            if r == destination[0] and c == destination[1]:
                return dist

            for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                r2 = r
                c2 = c
                next_dist = 0

                while isValid(r2 + dr, c2 + dc) and maze[r2 + dr][c2 + dc] == 0:
                    r2 += dr
                    c2 += dc
                    next_dist += 1

                if (r2, c2) in visited and visited[(r2, c2)] <= dist + next_dist:
                    continue

                visited[(r2, c2)] = dist + next_dist
                heapq.heappush(queue, [dist + next_dist, r2, c2])

        return -1
