# LC 731. My Calendar II

'''
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
'''

class MyCalendarTwo:

    def __init__(self):
        self.calendar = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for interval in self.overlaps:
            if start < interval[1] and interval[0] < end:
                return False

        for interval in self.calendar:
            if start < interval[1] and interval[0] < end:
                self.overlaps.append((max(start, interval[0]), min(end, interval[1])))

        self.calendar.append([start, end])
        return True

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

'''
NOTE: Can be solved using TreeMap (Boundary Count)
'''
