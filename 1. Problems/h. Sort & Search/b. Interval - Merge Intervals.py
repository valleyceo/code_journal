# Merging Intervals

'''
- Given an array of disjoint intervals with integer endpoints (sorted by increasing order) and an interval to be added.
- Return the union of the interval array and added interval
'''
Interval = collections.namedtuple('Interval', ('left', 'right'))

# O(n) complexity
def add_interval(disjoint_intervals: List[Interval],
                 new_interval: Interval) -> List[Interval]:

    i, result = 0, []

    # Processes intervals in disjoint_intervals which come before new_interval.
    while (i < len(disjoint_intervals)
           and new_interval.left > disjoint_intervals[i].right):
        result.append(disjoint_intervals[i])
        i += 1

    # Processes intervals in disjoint_intervals which overlap with new_interval.
    while (i < len(disjoint_intervals)
           and new_interval.right >= disjoint_intervals[i].left):
        # If [a, b] and [c, d] overlap, union is [min(a, c), max(b, d)].
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right))
        i += 1
    # Processes intervals in disjoint_intervals which come after new_interval.
    return result + [new_interval] + disjoint_intervals[i:]
