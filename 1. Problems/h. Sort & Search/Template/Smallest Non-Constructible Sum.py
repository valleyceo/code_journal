# Smallest Nonconstructible Sum

'''
- Given an array of positive integers
- Return the smallest number which is not the sum of a subset of elements of the array
'''

# O(nlogn) time | O(1) space
def smallest_nonconstructible_value(A: List[int]) -> int:

    max_constructible_value = 0
    for a in sorted(A):
        if a > max_constructible_value + 1:
            break
        max_constructible_value += a
    return max_constructible_value + 1


def smallest_nonconstructible_value_pythonic(A: List[int]) -> int:
    return functools.reduce(
        lambda max_val, a: max_val +
        (0 if a > max_val + 1 else a), sorted(A), 0) + 1
