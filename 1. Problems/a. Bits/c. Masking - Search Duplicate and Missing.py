# Find the Dublicate and Missing Elements

'''
- Given array of n integers (between 0 and n-1 inclusive)
- Ene element appears twice and one element is missing
- Find the missing and the duplicate element
'''

# Time commplexity: O(n) (actually O(3n))
# Space complexity: O(1)

DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing',
                                             ('duplicate', 'missing'))


def find_duplicate_missing(A: List[int]) -> DuplicateAndMissing:

    # Compute the XOR of all numbers from 0 to |A| - 1 and all entries in A.
    miss_xor_dup = functools.reduce(lambda v, i: v ^ i[0] ^ i[1], enumerate(A),
                                    0)

    # We need to find a bit that's set to 1 in miss_xor_dup. Such a bit must
    # exist if there is a single missing number and a single duplicated number
    # in A.
    #
    # The bit-fiddling assignment below sets all of bits in differ_bit
    # to 0 except for the least significant bit in miss_xor_dup that's 1.
    differ_bit, miss_or_dup = miss_xor_dup & (~(miss_xor_dup - 1)), 0
    for i, a in enumerate(A):
        # Focus on entries and numbers in which the differ_bit-th bit is 1.
        if i & differ_bit:
            miss_or_dup ^= i
        if a & differ_bit:
            miss_or_dup ^= a

    # miss_or_dup is either the missing value or the duplicated entry.
    # If miss_or_dup is in A, miss_or_dup is the duplicate;
    # otherwise, miss_or_dup is the missing value.
    return (DuplicateAndMissing(miss_or_dup, miss_or_dup
                                ^ miss_xor_dup) if miss_or_dup in A else
            DuplicateAndMissing(miss_or_dup ^ miss_xor_dup, miss_or_dup))

'''
- Process
1. Perform XOR to all idx and element values
2. Pick the least signicant bit to the value and redo XOR to all idx and element values that contains the bit
3. Now that you have found the value which is either the missing(1) or duplicate(3), search the array to separate missing and duplicate.
'''
