# LC 905. Sort Array By Parity

'''
Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
Example 2:

Input: nums = [0]
Output: [0]
'''
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start = 0
        end = len(A)-1

        while start < end:
            if A[start] % 2 == 0:
                start += 1
            else:
                A[start], A[end] = A[end], A[start]
                end -= 1

        return A
