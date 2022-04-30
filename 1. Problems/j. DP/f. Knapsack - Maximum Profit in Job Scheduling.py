# LC 1235. Maximum Profit in Job Scheduling

'''
We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.
'''

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:

        arr = []

        for s, e, p in zip(startTime, endTime, profit):
            arr.append([s, e, p])

        arr.sort(key = lambda x : x[1])
        dp = [[0, 0]] # endtime, max profit so far

        for s, e, p in arr:
            idx = bisect.bisect_left(dp, [s + 1]) - 1

            if dp[idx][1] + p > dp[-1][1]:
                dp.append([e, dp[idx][1] + p])

        return dp[-1][1]
