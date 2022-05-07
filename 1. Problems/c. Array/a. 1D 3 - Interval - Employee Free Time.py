# LC 759. Employee Free Time

'''
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted order.

(Even though we are representing Intervals in the form [x, y], the objects inside are Intervals, not lists or arrays. For example, schedule[0][0].start = 1, schedule[0][0].end = 2, and schedule[0][0][0] is not defined).  Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

Example 1:

Input: schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
Output: [[3,4]]
Explanation: There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.

Example 2:

Input: schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
Output: [[5,6],[7,9]]
'''

"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""
# O(NlogN) time | O(N) space
class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':

        flatten = []

        for intervals in schedule:
            for iv in intervals:
                flatten.append(iv)

        flatten.sort(key = lambda x : x.start)
        merged = []

        for iv in flatten:
            if merged and merged[-1].end >= iv.start:
                merged[-1].end = max(merged[-1].end, iv.end)
            else:
                merged.append(iv)

        free_intervals = []

        for i in range(1, len(merged)):
            free_intervals.append(Interval(merged[i-1].end, merged[i].start))

        return free_intervals
