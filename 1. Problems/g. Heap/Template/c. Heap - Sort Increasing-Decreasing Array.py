# Sort an Increasing-Decreasing Array

'''
- Given an array that is increasing and decreasing k times
- Sort the array
- Note: regular sorting takes O(nlogn) without taking advantage of k-inc-dec property
'''
def sort_k_increasing_decreasing_array(A: List[int]) -> List[int]:

    # Decomposes A into a set of sorted arrays.
    sorted_subarrays = []
    increasing, decreasing = range(2)
    subarray_type = increasing
    start_idx = 0
    for i in range(1, len(A) + 1):
        if (i == len(A) or  # A is ended. Adds the last subarray.
            (A[i - 1] < A[i] and subarray_type == decreasing) or
            (A[i - 1] >= A[i] and subarray_type == increasing)):
            sorted_subarrays.append(A[start_idx:i] if subarray_type ==
                                    increasing else A[i - 1:start_idx - 1:-1])
            start_idx = i
            subarray_type = (decreasing
                             if subarray_type == increasing else increasing)
    return merge_sorted_arrays(sorted_subarrays)

# Pythonic solution, uses a stateful object to trace the monotonic subarrays.
def sort_k_increasing_decreasing_array_pythonic(A: List[int]) -> List[int]:
    class Monotonic:
        def __init__(self):
            self._last = float('-inf')

        def __call__(self, curr):
            result = curr < self._last
            self._last = curr
            return result

    return merge_sorted_arrays([
        list(group)[::-1 if is_decreasing else 1]
        for is_decreasing, group in itertools.groupby(A, Monotonic())
    ])

'''
- Find and reverse the decreasing array
- Use merge sorted arrays function
'''
