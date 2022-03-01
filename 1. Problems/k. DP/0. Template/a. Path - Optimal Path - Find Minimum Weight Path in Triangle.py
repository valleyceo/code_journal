# Find the Minimum Weight Path in Triangle

'''
- Given a triangle of numbers (2D)
- Return minimum path from top to bottom
'''
# O(N^2) time | O(N) space
def minimum_path_weight(triangle: List[List[int]]) -> int:

    min_weight_to_curr_row = [0]
    for row in triangle:
        min_weight_to_curr_row = [
            row[j] + min(
                min_weight_to_curr_row[max(j - 1, 0)],
                min_weight_to_curr_row[min(j,
                                           len(min_weight_to_curr_row) - 1)])
            for j in range(len(row))
        ]
    return min(min_weight_to_curr_row)


def minimum_path_weight_pythonic(triangle):
    return min(
        functools.reduce(
            lambda result, tri: [
                r + min(a, b) for r, a, b in zip(tri, [float('inf')] + result,
                                                 result + [float('inf')])
            ], triangle, [0]))
