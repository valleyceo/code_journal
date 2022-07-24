# LC 1755. Closest Subsequence Sum

'''
You are given an integer array nums and an integer goal.

You want to choose a subsequence of nums such that the sum of its elements is the closest possible to goal. That is, if the sum of the subsequence's elements is sum, then you want to minimize the absolute difference abs(sum - goal).

Return the minimum possible value of abs(sum - goal).

Note that a subsequence of an array is an array formed by removing some elements (possibly all or none) of the original array.

Example 1:

Input: nums = [5,-7,3,5], goal = 6
Output: 0
Explanation: Choose the whole array as a subsequence, with a sum of 6.
This is equal to the goal, so the absolute difference is 0.
'''

class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:

        def possible_sums(arr):
            res = {0}

            for n in arr:
                res |= {n + n2 for n2 in res}

            return res

        left = sorted(possible_sums(nums[:len(nums)//2]))
        res = inf

        for n in possible_sums(nums[len(nums)//2:]):
            need = goal - n

            idx = bisect_left(left, need)
            if idx < len(left):
                res = min(res, left[idx] - need)

            if 0 < idx:
                res = min(res, need - left[idx - 1])

        return res
