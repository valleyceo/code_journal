# Compute Binomial Coefficient

'''
- Compute C(n, k) efficiently
- Make sure it does not overflow
'''
# O(nk) time | O(nk) space
@functools.lru_cache(None)
def compute_binomial_coefficient(n: int, k: int) -> int:

    if k in (0, n):
        return 1

    without_k = compute_binomial_coefficient(n - 1, k)
    with_k = compute_binomial_coefficient(n - 1, k - 1)
    return without_k + with_k


def compute_binomial_coefficients_space_efficient(n, k):
    k = min(k, n - k)
    table = [1] + [0] * k
    # C(i, j) = C(i - 1, j) + C(i - 1, j - 1).
    for i in range(1, n + 1):
        for j in reversed(range(1, min(i, k) + 1)):
            table[j] = table[j] + table[j - 1]
    return table[-1]

'''
Key formula: C(n, k) = C(n-1, k) + C(n-1, k-1)
'''
