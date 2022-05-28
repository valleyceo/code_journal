# LC 673. Number of Longest Increasing Subsequence

'''
Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].

Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
'''
# O(N^2) time | O(1) space
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [[1, 1] for _ in range(len(nums))]
        res = 1
        max_len = 1

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:

                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i][0] = dp[j][0] + 1
                        dp[i][1] = dp[j][1]
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i][1] += dp[j][1]

            if dp[i][0] > max_len:
                max_len = dp[i][0]
                res = dp[i][1]
            elif dp[i][0] == max_len:
                res += dp[i][1]

        return res
