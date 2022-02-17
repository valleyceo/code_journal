# Compute a Random Subset

'''
- Given a positive integer n and a size k <= n
- Return a size-k subset from {0, 1, 2, ..., n-1}
'''
# time: O(k) | space: O(k)
def random_subset(n: int, k: int) -> List[int]:

    changed_elements: Dict[int, int] = {}
    for i in range(k):
        # Generate a random index between i and n - 1, inclusive.
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx_mapped
    return [changed_elements[i] for i in range(k)]

'''
- picks a random number and creates cyclic hash map
- if same number gets picked, merges with parts
- Note: this algorithm ends up creating unique numbers both in .first (0-k) and .second (0-n) in random orders
'''
