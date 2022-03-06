# 57. Insert Interval

'''
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:

0 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^5
intervals is sorted by starting in ascending order.
newInterval.length == 2
0 <= start <= end <= 10^5
'''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        idx = 0
        n = len(intervals)
        res = []

        while idx < n and intervals[idx][0] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1

        if not res or res[-1][1] < newInterval[0]:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], newInterval[1])

        while idx < n:
            if res[-1][1] < intervals[idx][0]:
                res.append(intervals[idx])
            else:
                res[-1][1] = max(res[-1][1], intervals[idx][1])

            idx += 1

        return res

'''
NOTE: Binary search does not work because interval editing requires O(N) complexity
'''
