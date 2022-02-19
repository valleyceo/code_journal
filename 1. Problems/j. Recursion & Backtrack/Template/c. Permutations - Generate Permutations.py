# Permutations

'''
- Given an array of distinct integers
- Generate all permutations of that array
'''

# O(n x n!) time
def permutations(A: List[int]) -> List[List[int]]:
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return

        # Try every possibility for A[i].
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i]
            # Generate all permutations for A[i + 1:].
            directed_permutations(i + 1)
            A[i], A[j] = A[j], A[i]

    result: List[List[int]] = []
    directed_permutations(0)
    return result

'''
C(n) = 1 + n * C(n-1) = 1 + n + n(n-1) + n(n-1)(n-2) + ... + !n =~ (e-1)!n (e: euler's number)
'''
