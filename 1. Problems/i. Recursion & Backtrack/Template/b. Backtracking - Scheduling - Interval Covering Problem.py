# Interval Covering Problem

'''
- Given a set of closed intervals
- Find minimum sized set of numbers that covers all intervals
'''
Interval = collections.namedtuple('Interval', ('left', 'right'))

# O(nlogn) time
def find_minimum_visits(intervals: List[Interval]) -> int:

    # Sort intervals based on the right endpoints.
    intervals.sort(key=operator.attrgetter('right'))
    last_visit_time, num_visits = float('-inf'), 0
    for interval in intervals:
        if interval.left > last_visit_time:
            # The current right endpoint, last_visit_time, will not cover any
            # more intervals.
            last_visit_time = interval.right
            num_visits += 1
    return num_visits

'''
- Idea:
	1. Sort by right
	2. Iterate through item
	3. keep a pointer from -inf, and whenever a new interval.left is bigger, set it to the interval.right (this creates new interval)
'''
