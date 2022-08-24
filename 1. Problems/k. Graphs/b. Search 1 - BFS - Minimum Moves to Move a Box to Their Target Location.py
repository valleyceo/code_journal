# LC 1263. Minimum Moves to Move a Box to Their Target Location

'''
A storekeeper is a game in which the player pushes boxes around in a warehouse trying to get them to target locations.

The game is represented by an m x n grid of characters grid where each element is a wall, floor, or box.

Your task is to move the box 'B' to the target position 'T' under the following rules:

The character 'S' represents the player. The player can move up, down, left, right in grid if it is a floor (empty cell).
The character '.' represents the floor which means a free cell to walk.
The character '#' represents the wall which means an obstacle (impossible to walk there).
There is only one box 'B' and one target cell 'T' in the grid.
The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box. This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.
'''

class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "T":
                    target = (i, j)

                if grid[i][j] == "B":
                    box = (i, j)

                if grid[i][j] == "S":
                    person = (i, j)

        def valid(x, y):
            return 0 <= x < n and 0 <= y < m and grid[x][y] != "#"

        def check(curr, dest, box):
            queue = deque([curr])
            visited = set()

            while queue:
                pos = queue.popleft()

                if pos == dest:
                    return True

                i, j = pos

                for i2, j2 in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                    if not valid(i2, j2) or (i2, j2) in visited or (i2, j2) == box:
                        continue

                    visited.add((i2, j2))
                    queue.append((i2, j2))

            return False

        q = deque([(0, box, person)])
        vis = {tuple(box + person)}

        while q:
            dist, box, person = q.popleft()

            if box == target:
                return dist

            b_coord = [(box[0] + 1, box[1]), (box[0] - 1, box[1]), (box[0], box[1] - 1), (box[0], box[1] + 1)]
            p_coord = [(box[0] - 1, box[1]), (box[0] + 1, box[1]), (box[0], box[1] + 1), (box[0], box[1] - 1)]

            for box2, person2 in zip(b_coord, p_coord):
                if valid(*box2) and box2 + box not in vis:
                    if valid(*person2) and check(person, person2, box):
                        vis.add(box2 + box)
                        q.append((dist + 1, box2, box))

        return -1
