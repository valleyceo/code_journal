# Compute Random Permutation

'''
Create uniformly random permutations of {0, 1, ..., n-1}
'''

# Time: O(n), no extra spaces
def compute_random_permutation(n: int) -> List[int]:

    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation
