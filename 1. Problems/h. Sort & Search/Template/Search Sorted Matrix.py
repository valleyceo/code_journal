# Search in a 2D Sorted Array

'''
- Given an integer and 2D array where its rows and columns are sorted in nondecreaing order.
- Check whether the number appears in the array.
'''

# O(m + n) time
def matrix_search(A: List[List[int]], x: int) -> bool:

    row, col = 0, len(A[0]) - 1  # Start from the top-right corner.
    # Keeps searching while there are unclassified rows and columns.
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1  # Eliminate this row.
        else:  # A[row][col] > x.
            col -= 1  # Eliminate this column.
    return False

'''
- Starting from top-right, move down if value is bigger, or left if smaller.
- This will weave through all values close to the seached number and guarantee crossover.

'''
