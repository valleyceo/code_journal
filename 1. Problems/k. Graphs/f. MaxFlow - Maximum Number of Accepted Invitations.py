# LC 1820. Maximum Number of Accepted Invitations

'''
There are m boys and n girls in a class attending an upcoming party.

You are given an m x n integer matrix grid, where grid[i][j] equals 0 or 1. If grid[i][j] == 1, then that means the ith boy can invite the jth girl to the party. A boy can invite at most one girl, and a girl can accept at most one invitation from a boy.

Return the maximum possible number of accepted invitations.

Example 1:

Input: grid = [[1,1,1],
               [1,0,1],
               [0,0,1]]
Output: 3
Explanation: The invitations are sent as follows:
- The 1st boy invites the 2nd girl.
- The 2nd boy invites the 1st girl.
- The 3rd boy invites the 3rd girl.
'''

class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        return self.hungarianAlgorithm2(grid)

    def hungarianAlgorithm(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matches = {}

        def dfs(boy, visited):


            for girl in range(n):

                if grid[boy][girl] and girl not in visited:
                    visited.add(girl)

                    if girl not in matches or dfs(matches[girl], visited):
                        matches[girl] = boy
                        return True

            return False

        for boy in range(m):
            dfs(boy, set())

        return len(matches)

    def hungarianAlgorithm2(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        matches = [-1] * n
        res = 0

        def dfs(i, seen):

            for j in range(n):
                if grid[i][j] and not seen[j]:
                    seen[j] = True

                    if matches[j] == -1 or dfs(matches[j], seen):
                        matches[j] = i
                        return True

            return False

        for i in range(m):
            seen = [False] * n

            if dfs(i, seen):
                res += 1

        return res
