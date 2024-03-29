# Find The Length of a Longest Contained Interval

'''
- Given an array
- Return the size of a largest subset of integers in the array

- Ex: < 3, -2, 7, 9, 8, 1, 2, 0, -1, 5, 8 >
- output: < -2, -1, 0, 1, 2, 3 > -> 6
'''

# O(n) time | O(n) space
def longest_contained_range(A: List[int]) -> int:

    # unprocessed_entries records the existence of each entry in A.
    unprocessed_entries = set(A)

    max_interval_size = 0
    while unprocessed_entries:
        a = unprocessed_entries.pop()

        # Finds the lower bound of the largest range containing a.
        lower_bound = a - 1
        while lower_bound in unprocessed_entries:
            unprocessed_entries.remove(lower_bound)
            lower_bound -= 1

        # Finds the upper bound of the largest range containing a.
        upper_bound = a + 1
        while upper_bound in unprocessed_entries:
            unprocessed_entries.remove(upper_bound)
            upper_bound += 1

        max_interval_size = max(max_interval_size,
                                upper_bound - lower_bound - 1)
    return max_interval_size
