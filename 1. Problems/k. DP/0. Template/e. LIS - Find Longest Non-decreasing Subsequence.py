# Find the Longest Nondecreasing Subsequence

'''
- Given an array of numbers
- Return the length of longest nondecreasing subsequence

- Note: non-decreasing sequence are not required to immediately follow each other (can skip)
- Ex: {0,8,4,12,2,10,6,14,1,9} -> {0,4,10,14} or {0,2,6,9}
'''

# O(n^2) time | O(n) space
def longest_nondecreasing_subsequence_length(A: List[int]) -> int:

    # max_length[i] holds the length of the longest nondecreasing subsequence
    # of A[:i + 1].
    max_length = [1] * len(A)
    for i in range(1, len(A)):
        max_length[i] = 1 + max(
            (max_length[j] for j in range(i) if A[i] >= A[j]), default=0)
    return max(max_length)
