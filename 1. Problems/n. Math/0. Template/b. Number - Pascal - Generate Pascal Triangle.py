# Generate Pascal Triangle

'''

  1
 1 1
1 2 1
...

'''
# time: O(n^2), space: O(n^2)
def generate_pascal_triangle(n: int) -> List[List[int]]:

    result = [[1] * (i + 1) for i in range(n)]
    for i in range(n):
        for j in range(1, i):
            # Sets this entry to the sum of the two above adjacent entries.
            result[i][j] = result[i - 1][j - 1] + result[i - 1][j]
    return result

'''
- can use combinatorics (n choose i)
'''
