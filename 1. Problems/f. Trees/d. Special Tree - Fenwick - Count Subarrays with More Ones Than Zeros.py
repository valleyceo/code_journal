# LC 2031. Count Subarrays With More Ones Than Zeros

'''
You are given a binary array nums containing only the integers 0 and 1. Return the number of subarrays in nums that have more 1's than 0's. Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous sequence of elements within an array.

Example 1:

Input: nums = [0,1,1,0,1]
Output: 9
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1], [1], [1]
The subarrays of size 2 that have more ones than zeros are: [1,1]
The subarrays of size 3 that have more ones than zeros are: [0,1,1], [1,1,0], [1,0,1]
The subarrays of size 4 that have more ones than zeros are: [1,1,0,1]
The subarrays of size 5 that have more ones than zeros are: [0,1,1,0,1]

Example 2:

Input: nums = [0]
Output: 0
Explanation:
No subarrays have more ones than zeros.

Example 3:

Input: nums = [1]
Output: 1
Explanation:
The subarrays of size 1 that have more ones than zeros are: [1]
'''
class Solution:
    def subarraysWithMoreZerosThanOnes(self, nums: List[int]) -> int:
        mod = 10**9 + 7

        res = 0
        prefix = 0
        bit = BIT(len(nums))
        bit.add(0, 1)

        for n in nums:
            prefix += -1 if n == 0 else 1
            res += bit.prefixSum(prefix - 1)
            res %= mod

            bit.add(prefix, 1)

        return res


class BIT():
    def __init__(self, n: int):
        self.n = n
        self.sums = [0] * (2 * n + 1)

    def add(self, i: int, delta: int) -> None:
        i += self.n + 1  # re-mapping
        while i < len(self.sums):
            self.sums[i] += delta
            i += i & -i

    def prefixSum(self, i: int) -> int:
        i += self.n + 1  # re-mapping
        sum = 0
        while i > 0:
            sum += self.sums[i]
            i -= i & -i
        return sum
