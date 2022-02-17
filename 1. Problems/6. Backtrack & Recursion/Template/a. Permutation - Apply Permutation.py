# Apply Permutation

'''
- Given array A and permutation array P, apply P to A
- Ex. P = < 2,0,1,3 >, A = < a,b,c,d > => A_new = < b, c, a, d >
'''

# O(n) time | O(1) space
def apply_permutation(perm: List[int], A: List[int]) -> None:

    for i in range(len(A)):
        while perm[i] != i:
            A[perm[i]], A[i] = A[i], A[perm[i]]
            perm[perm[i]], perm[i] = perm[i], perm[perm[i]]


'''
- Swap with permuted next element, keep track by subtracting -size(P) (add them later)
- Two loops: 1. loop over each array, 2. loop over next permuted element
'''
