# LC 2127. Maximum Employees to Be Invited to a Meeting

'''
A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person and they will attend the meeting only if they can sit next to their favorite person at the table. The favorite person of an employee is not themself.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the maximum number of employees that can be invited to the meeting.
'''
# O(n) time | O(n) space
class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        indeg = [0] * n
        visited = [False] * n
        queue = deque([])
        dp = [0] * n

        for i in range(n):
            indeg[favorite[i]] += 1

        for i in range(n):
            if indeg[i] == 0:
                visited[i] = True
                queue.append(i)

        while queue:
            p = queue.popleft()
            fav = favorite[p]
            dp[fav] = max(dp[fav], dp[p] + 1)
            indeg[fav] -= 1

            if indeg[fav] == 0:
                visited[fav] = True
                queue.append(fav)

        type1 = 0
        type2 = 0

        for p in range(n):
            if not visited[p]:
                curr = p
                length = 0

                while not visited[curr]:
                    visited[curr] = True
                    curr = favorite[curr]
                    length += 1

                if length == 2:
                    type1 += dp[p] + dp[favorite[p]] + 2
                else:
                    type2 = max(type2, length)

        return max(type1, type2)
