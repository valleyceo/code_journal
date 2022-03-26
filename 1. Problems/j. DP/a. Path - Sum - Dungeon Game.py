# LC 174. Dungeon Game

'''
The demons had captured the princess and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of m x n rooms laid out in a 2D grid. Our valiant knight was initially positioned in the top-left room and must fight his way through dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons (represented by negative integers), so the knight loses health upon entering these rooms; other rooms are either empty (represented as 0) or contain magic orbs that increase the knight's health (represented by positive integers).

To reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

Return the knight's minimum initial health so that he can rescue the princess.

Note that any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        return self.DP(dungeon)

    def DP(self, dungeon: List[List[int]]) -> int:
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        def get_min(curr_cell, next_row, next_col):
            if next_row >= R or next_col >= C:
                return float('inf')

            next_cell = dp[next_row][next_col]
            return max(1, next_cell - curr_cell)

        R = len(dungeon)
        C = len(dungeon[0])

        dp = [[float('inf') for _ in range(C)] for _ in range(R)]

        for i in reversed(range(R)):
            for j in reversed(range(C)):
                right = get_min(dungeon[i][j], i, j + 1)
                down = get_min(dungeon[i][j], i + 1, j)
                min_val = min(right, down)

                if min_val != float('inf'):
                    min_health = min_val
                else:
                    min_health = 1 if dungeon[i][j] >= 0 else (1 - dungeon[i][j])

                dp[i][j] = min_health

        return dp[0][0]
