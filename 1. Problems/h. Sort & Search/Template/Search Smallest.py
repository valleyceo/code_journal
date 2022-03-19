# Search a Cyclically Sorted Array

'''
- Given a cyclically sorted array
- Find the smallest element and return the index
'''

# O(logn) time
def search_smallest(A: List[int]) -> int:

    left, right = 0, len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            # Minimum must be in A[mid + 1:right + 1].
            left = mid + 1
        else:  # A[mid] < A[right].
            # Minimum cannot be in A[mid + 1:right + 1] so it must be in A[left:mid + 1].
            right = mid
    # Loop ends when left == right.
    return left
