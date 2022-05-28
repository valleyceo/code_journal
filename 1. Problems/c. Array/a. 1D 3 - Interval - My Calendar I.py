# LC 729. My Calendar I

'''
You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection (i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

MyCalendar() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a double booking. Otherwise, return false and do not add the event to the calendar.
'''

# Brute force
# O(N^2) time | O(N) space
class MyCalendar:

    def __init__(self):
        self.events = []

    def book(self, start: int, end: int) -> bool:

        for s, e in self.events:
            if s < end and start < e:
                return False

        self.events.append((start, end))
        return True

# Binary Search Tree Solution (can avoid worst time by using balanced tree)
# O(NlogN) time, O(N^2) worst time (skewed tree) | O(N) space
class Node:
    __slots__ = "start", "end", "left", "right"

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None

    def insert(self, node):
        if node.start >= self.end:
            if not self.right:
                self.right = node
                return True

            return self.right.insert(node)

        elif node.end <= self.start:
            if not self.left:
                self.left = node
                return True

            return self.left.insert(node)

        return False


class MyCalendar:

    def __init__(self):
        self.root = None

    def book(self, start: int, end: int) -> bool:
        if self.root is None:
            self.root = Node(start, end)
            return True
        else:
            return self.root.insert(Node(start, end))
