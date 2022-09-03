# LC 2276. Count Integers in Intervals

'''
Given an empty set of intervals, implement a data structure that can:

Add an interval to the set of intervals.
Count the number of integers that are present in at least one interval.
Implement the CountIntervals class:

CountIntervals() Initializes the object with an empty set of intervals.
void add(int left, int right) Adds the interval [left, right] to the set of intervals.
int count() Returns the number of integers that are present in at least one interval.
Note that an interval [left, right] denotes all the integers x where left <= x <= right.
'''

from sortedcontainers import SortedList

class CountIntervals:

    def __init__(self):
        self.cnt = 0
        self.intervals = SortedList()

    def add(self, left: int, right: int) -> None:
        idx = self.intervals.bisect_left((left, right))

        while idx < len(self.intervals) and self.intervals[idx][0] <= right:
            l, r = self.intervals.pop(idx)
            self.cnt -= r - l + 1
            right = max(right, r)

        if idx > 0 and left <= self.intervals[idx - 1][1]:
            l, r = self.intervals.pop(idx - 1)
            self.cnt -= r - l + 1
            left = l
            right = max(right, r)

        self.cnt += right - left + 1
        self.intervals.add((left, right))

    def count(self) -> int:
        return self.cnt
