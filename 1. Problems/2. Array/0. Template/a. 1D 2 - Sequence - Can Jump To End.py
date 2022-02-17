# Advance Through an Array

'''
- Array of n integers
- A[i] denotes the maximum you can advance from index i
- return whether it is possible to advance to the last index starting from beginning of array
'''

# O(n) time | O(1) space
def can_reach_end(A: List[int]) -> bool:

    furthest_reach_so_far, last_index = 0, len(A) - 1
    i = 0
    while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
        furthest_reach_so_far = max(furthest_reach_so_far, A[i] + i)
        i += 1
    return furthest_reach_so_far >= last_index
