# LC 1296. Divide Array in Sets of K Consecutive Numbers

'''
Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
'''

from collections import OrderedDict

# O(NlogN + NK) amortized time | O(N) space
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)

        for n in sorted(count):
            if count[n] > 0:

                for seq in reversed(range(n, n + k)):
                    count[seq] -= count[n]

                    if count[seq] < 0:
                        return False

        return True
