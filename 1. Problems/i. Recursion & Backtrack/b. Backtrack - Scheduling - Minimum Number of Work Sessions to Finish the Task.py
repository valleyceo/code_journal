# LC 1986. Minimum Number of Work Sessions to Finish the Tasks

'''
There are n tasks assigned to you. The task times are represented as an integer array tasks of length n, where the ith task takes tasks[i] hours to finish. A work session is when you work for at most sessionTime consecutive hours and then take a break.

You should finish the given tasks in a way that satisfies the following conditions:

If you start a task in a work session, you must complete it in the same work session.
You can start a new task immediately after finishing the previous one.
You may complete the tasks in any order.
Given tasks and sessionTime, return the minimum number of work sessions needed to finish all the tasks following the conditions above.

The tests are generated such that sessionTime is greater than or equal to the maximum element in tasks[i].

Example 1:

Input: tasks = [1,2,3], sessionTime = 3
Output: 2
Explanation: You can finish the tasks in two work sessions.
- First work session: finish the first and the second tasks in 1 + 2 = 3 hours.
- Second work session: finish the third task in 3 hours.
'''

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        cache = {}

        def backtrack(idx, tlist):
            if idx == len(tasks):
                return len(tlist)

            key = (idx, str(sorted(tlist)))
            if key in cache:
                return cache[key]

            min_len = float('inf')

            for i in range(len(tlist)):
                if tlist[i] + tasks[idx] <= sessionTime:

                    tlist[i] += tasks[idx]
                    min_len = min(min_len, backtrack(idx + 1, tlist))
                    tlist[i] -= tasks[idx]

            tlist.append(tasks[idx])
            min_len = min(min_len, backtrack(idx + 1, tlist))
            tlist.pop()

            cache[key] = min_len
            return min_len

        return backtrack(0, [0])
