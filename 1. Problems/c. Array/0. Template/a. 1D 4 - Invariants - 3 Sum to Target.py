# The 3-Sum Problem

'''
- Given an array and a target number
- Determine if there are three entries that add up to the target number
'''

# O(N^2) time | O(N) space
def has_three_sum(A: List[int], t: int) -> bool:

    A.sort()
    # Finds if the sum of two numbers in A equals to t - a.
    return any(has_two_sum(A, t - a) for a in A)
