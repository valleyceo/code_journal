# LC 715. Range Module

'''
A Range Module is a module that tracks ranges of numbers. Design a data structure to track the ranges represented as half-open intervals and query about them.

A half-open interval [left, right) denotes all the real numbers x where left <= x < right.

Implement the RangeModule class:

RangeModule() Initializes the object of the data structure.
void addRange(int left, int right) Adds the half-open interval [left, right), tracking every real number in that interval. Adding an interval that partially overlaps with currently tracked numbers should add any numbers in the interval [left, right) that are not already tracked.
boolean queryRange(int left, int right) Returns true if every real number in the interval [left, right) is currently being tracked, and false otherwise.
void removeRange(int left, int right) Stops tracking every real number currently being tracked in the half-open interval [left, right).
'''

# O(N) add/remove, O(logN) query time | O(N) space
class RangeModule:

    def __init__(self):
        self.intervals = []

    def addRange(self, left: int, right: int) -> None:
        insort(self.intervals, [left, right])
        res = [self.intervals[0]]

        for interval in self.intervals[1:]:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)

        self.intervals = res

    def queryRange(self, left: int, right: int) -> bool:
        idx = bisect.bisect(self.intervals, [left, float('inf')])

        if not self.intervals:
            return False

        if self.intervals and idx == 0:
            return False

        return self.intervals[idx - 1][1] >= right

    def removeRange(self, left: int, right: int) -> None:
        res = []

        for interval in self.intervals:
            if left <= interval[0] and interval[1] <= right:
                continue
            elif interval[1] <= left or right <= interval[0]:
                res.append(interval)
            elif interval[1] < right:
                res.append([interval[0], left])
            elif left < interval[0]:
                res.append([right, interval[1]])
            else:
                res.append([interval[0], left])
                res.append([right, interval[1]])

        self.intervals = res

# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
