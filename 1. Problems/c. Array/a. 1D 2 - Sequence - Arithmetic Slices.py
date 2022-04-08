# LC 413. Arithmetic Slices

'''
An integer array is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1,3,5,7,9], [7,7,7,7], and [3,-1,-5,-9] are arithmetic sequences.
Given an integer array nums, return the number of arithmetic subarrays of nums.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We have 3 arithmetic slices in nums: [1, 2, 3], [2, 3, 4] and [1,2,3,4] itself.

Example 2:

Input: nums = [1]
Output: 0
'''
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        return self.cleanerSolution(nums)

    def mySolution(self, nums: List[int]) -> int:
        def count_combinations(n):
            return (n) * (n - 1) // 2

        if len(nums) < 3:
            return 0

        prev_diff = nums[1] - nums[0]
        count = 1
        res = 0

        for i in range(2, len(nums)):
            curr_diff = nums[i] - nums[i-1]
            if curr_diff == prev_diff:
                count += 1
            else:
                if count > 1:
                    res += count_combinations(count)

                count = 1
                prev_diff = curr_diff

        if count > 1:
            res += count_combinations(count)

        return res

    def cleanerSolution(self, nums: List[int]) -> int:
        dp = 0
        res = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp = dp + 1
                res += dp
            else:
                dp = 0

        return res
