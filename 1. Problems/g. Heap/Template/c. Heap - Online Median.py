# Compute the Median of Online Data

'''
- Given stream of numbers
- Design a running median of sequence

Note: You cannot back up to read earlier value
'''
# O(logn) insertion time | O(n) space
def online_median(sequence: Iterator[int]) -> List[float]:

    # min_heap stores the larger half seen so far.
    min_heap: List[int] = []
    # max_heap stores the smaller half seen so far.
    # values in max_heap are negative
    max_heap: List[int] = []
    result = []

    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        # Ensure min_heap and max_heap have equal number of elements if an even
        # number of elements is read; otherwise, min_heap must have one more
        # element than max_heap.
        if len(max_heap) > len(min_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

        result.append(0.5 * (min_heap[0] + (-max_heap[0])) if len(min_heap) ==
                      len(max_heap) else min_heap[0])
    return result


def online_median_wrapper(sequence):
    return online_median(iter(sequence))
