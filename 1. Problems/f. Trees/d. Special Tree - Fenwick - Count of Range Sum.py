# 327. Count of Range Sum

'''
Given an integer array nums and two integers lower and upper, return the number of range sums that lie in [lower, upper] inclusive.

Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j inclusive, where i <= j.

Example 1:

Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.

Example 2:

Input: nums = [0], lower = 0, upper = 0
Output: 1
'''

from itertools import accumulate
from bisect import bisect_left, bisect_right

class BIT():
    def __init__(self, N):
        self.N = N + 1
        self.bit = [0] * self.N

    # add val to self.data[index]
    def update(self, index, value = 1):

        while index < self.N:
            self.bit[index] += value
            index = (index | (index - 1)) + 1

    def query(self, index):
        ans = 0
        while index > 0:
            ans += self.bit[index]
            index &= index - 1
        return ans


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        res = 0
        preSum = [0] + list(accumulate(nums))
        bit = BIT(n + 1)
        sortedSum = sorted(preSum)

        for s in preSum:
            upper_rank = bisect_right(sortedSum, s - lower)
            lower_rank = bisect_left(sortedSum, s - upper)
            res += bit.query(upper_rank) - bit.query(lower_rank)
            bit.update(bisect_left(sortedSum, s) + 1)

        return res
