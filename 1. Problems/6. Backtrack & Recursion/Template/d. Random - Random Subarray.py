# Random Subarray

'''
- Given array A, create random subarray of size k
'''

# Time: O(n), Space: O(1)
def random_sampling(k: int, A: List[int]) -> None:

    for i in range(k):
        # Generate a random index in [i, len(A) - 1].
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
