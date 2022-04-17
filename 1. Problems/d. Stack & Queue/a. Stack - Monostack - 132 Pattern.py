# 456. 132 Pattern

'''
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.

Example 1:

Input: nums = [1,2,3,4]
Output: false
Explanation: There is no 132 pattern in the sequence.

Example 2:

Input: nums = [3,1,4,2]
Output: true
Explanation: There is a 132 pattern in the sequence: [1, 4, 2].

Example 3:

Input: nums = [-1,3,2,0]
Output: true
Explanation: There are three 132 patterns in the sequence: [-1, 3, 2], [-1, 3, 0] and [-1, 2, 0].
'''
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        return self.monostack(nums)

    # O(N^3) time | O(1) space
    def bruteForceTLE(self, nums: List[int]) -> bool:
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] < nums[k] < nums[j]:
                        return True

        return False

    # O(N^2) time | O(1) space
    def bruteForceImprovedTLE(self, nums: List[int]) -> bool:
        n = len(nums)
        nums_i = float('inf')

        for j in range(n):
            nums_i = min(nums_i, nums[j])

            for k in range(j + 1, n):
                if nums_i < nums[k] < nums[j]:
                    return True

        return False

    def intervalSolutionTLE(self, nums: List[int]) -> bool:
        n = len(nums)
        intervals = []
        i = 1
        min_after_peak_idx = 0

        for i in range(1, n):

            if nums[i - 1] > nums[i]:
                if min_after_peak_idx < i - 1:
                    intervals.append([nums[min_after_peak_idx], nums[i - 1]])

                min_after_peak_idx = i

            for interval in intervals:
                if interval[0] < nums[i] < interval[1]:
                    return True

        return False

    # O(n) time | O(n) space
    def monostack(self, nums: List[int]) -> bool:
        n = len(nums)

        if n < 3:
            return False

        stack = []
        min_dp = [-1] * len(nums)
        min_dp[0] = nums[0]

        for i in range(1, n):
            min_dp[i] = min(min_dp[i-1], nums[i])

        for i in range(n - 1, -1, -1):
            if nums[i] == min_dp[i]:
                continue

            while stack and stack[-1] <= min_dp[i]:
                stack.pop()

            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])

        return False
