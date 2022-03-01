# Find Max Subarray

'''
- Given an array
- Return a subarray with maximum sum
'''
# O(n) time | O(1) space
def find_maximum_subarray(A: List[int]) -> int:

    max_seen = max_end = 0
    for a in A:
        max_end = max(a, a + max_end)
        max_seen = max(max_seen, max_end)
    return max_seen


'''
ex. [1 2 3 -3 -3 2 10 -12 3 4]
run [1 3 6  3  0 2 13  1  4 8]
min [1 1 1  1  0 0  0  0  0 0]
max [0 2 5  2  0 2 13  1  4 8] -> max: 13

- not an array, updates every iteration to next step
- similar to stock market. you buy at the lowest running sum and find (running_sum - min)
'''
