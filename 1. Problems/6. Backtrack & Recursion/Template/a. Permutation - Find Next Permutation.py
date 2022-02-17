# Find Next Permutation

'''
- takes a permutation and returns next permutation under dictionary order
- ex: < 6, 2, 1, 5, 4, 3, 0> -> < 6, 2, 3, 0, 1, 4, 5 >
'''

# O(n) time | O(1) space
def next_permutation(perm: List[int]) -> List[int]:

    # Find the first entry from the right that is smaller than the entry
    # immediately after it.
    inversion_point = len(perm) - 2
    while (inversion_point >= 0
           and perm[inversion_point] >= perm[inversion_point + 1]):
        inversion_point -= 1
    if inversion_point == -1:
        return []  # perm is the last permutation.

    # Swap the smallest entry after index inversion_point that is greater than
    # perm[inversion_point]. Since entries in perm are decreasing after
    # inversion_point, if we search in reverse order, the first entry that is
    # greater than perm[inversion_point] is the entry to swap with.
    for i in reversed(range(inversion_point + 1, len(perm))):
        if perm[i] > perm[inversion_point]:
            perm[inversion_point], perm[i] = perm[i], perm[inversion_point]
            break

    # Entries in perm must appear in decreasing order after inversion_point,
    # so we simply reverse these entries to get the smallest dictionary order.
    perm[inversion_point + 1:] = reversed(perm[inversion_point + 1:])
    return perm

'''
- General algorithm
1. Find the first decreasing number (k) from back to start order
2. Find the next smallest number than k
3. Swap the two numbers
4. Reverse the sequence after position k
'''
