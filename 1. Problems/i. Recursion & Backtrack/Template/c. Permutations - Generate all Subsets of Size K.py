# Generate All Subsets of Size K

'''
- Given integer k and n
- Find all subset of size k from set {1, 2, ..., n}
'''

# O(n(n, k)) time
def combinations(n: int, k: int) -> List[List[int]]:
    def directed_combinations(offset, partial_combination):
        if len(partial_combination) == k:
            result.append(partial_combination.copy())
            return

        # Generate remaining combinations over {offset, ..., n - 1} of size
        # num_remaining.
        num_remaining = k - len(partial_combination)
        i = offset
        while i <= n and num_remaining <= n - i + 1:
            directed_combinations(i + 1, partial_combination + [i])
            i += 1

    result: List[List[int]] = []
    directed_combinations(1, [])
    return result


def combinations_pythonic(n, k):
    result = [[]]
    for _ in range(k):
        result = [[i] + c for c in result
                  for i in range(1, c[0] if c else n + 1)]
    return result
