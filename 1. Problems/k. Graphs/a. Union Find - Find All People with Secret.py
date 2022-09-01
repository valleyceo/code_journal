# LC 2092. Find All People With Secret

'''
You are given an integer n indicating there are n people numbered from 0 to n - 1. You are also given a 0-indexed 2D integer array meetings where meetings[i] = [xi, yi, timei] indicates that person xi and person yi have a meeting at timei. A person may attend multiple meetings at the same time. Finally, you are given an integer firstPerson.

Person 0 has a secret and initially shares the secret with a person firstPerson at time 0. This secret is then shared every time a meeting takes place with a person that has the secret. More formally, for every meeting, if a person xi has the secret at timei, then they will share the secret with person yi, and vice versa.

The secrets are shared instantaneously. That is, a person may receive the secret and share it with people in other meetings within the same time frame.

Return a list of all the people that have the secret after all the meetings have taken place. You may return the answer in any order.
'''

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        roots = [i for i in range(n)]
        roots[firstPerson] = 0

        def find(x):
            if roots[x] == x:
                return x
            roots[x] = find(roots[x])
            return roots[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)

            if rx != ry:
                if rx == 0 or ry == 0:
                    roots[rx] = roots[ry] = 0

                else:
                    roots[y] = rx

        meetings.sort(key = lambda x : x[2])
        N = len(meetings)
        idx = 0

        while idx < N:
            same_time_meetings = [meetings[idx]]

            while idx < N - 1 and meetings[idx + 1][2] == meetings[idx][2]:
                idx += 1
                same_time_meetings.append(meetings[idx])


            for n1, n2, time in same_time_meetings:
                union(n1, n2)

            # Reset union if it's not connected to 0
            for n1, n2, time in same_time_meetings:
                rx = find(n1)

                if rx != 0:
                    roots[n1] = n1
                    roots[n2] = n2

            idx += 1

        return [i for i in range(n) if find(i) == 0]
