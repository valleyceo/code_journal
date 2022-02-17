# Rearrange Alternation

'''
- Take an array A of n numbers, and rearrange A's elements to get a new array B such that:

B[0] <= B[1] >= B[2] <= B[3] >= B[4] ...
'''

# O(n) time | O(1) space
def rearrange(A: List[int]) -> None:

    for i in range(len(A)):
        A[i:i + 2] = sorted(A[i:i + 2], reverse=bool(i % 2))

'''
- Better than sort and swap O(nlog(n))
- Similar to median finding
'''
