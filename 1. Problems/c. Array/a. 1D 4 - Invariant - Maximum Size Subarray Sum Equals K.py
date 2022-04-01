# LC 325. Maximum Size Subarray Sum Equals k

'''
Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.

Example 1:

Input: nums = [1,-1,5,-2,3], k = 3
Output: 4
Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

Example 2:

Input: nums = [-2,-1,2,1], k = 1
Output: 2
Explanation: The subarray [-1, 2] sums to 1 and is the longest.
'''
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        return self.prefixSumOptimized(nums, k)

    # O(n^2) time | O(1) space
    def naive(self, nums: List[int], k: int) -> int:
        maxLen = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)+1):
                if sum(nums[i:j]) == k:
                    maxLen = max(maxLen, j - i)

        return maxLen

    # O(n) time | O(n) space
    # Use prefix sum and hashmap
    def prefixSum(self, nums: List[int], k: int) -> int:

        prefix = [0] * (len(nums) + 1)

        for i in range(1, len(nums) + 1):
            prefix[i] = prefix[i-1] + nums[i - 1]

        mp = {}
        res = 0
        for i, p in enumerate(prefix):
            if p - k in mp:
                res = max(res, i - mp[p-k])

            if p not in mp:
                mp[p] = i

        return res

    # O(n) time | O(1) space
    def prefixSumOptimized(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        mp = {0: 0}
        res = 0

        for i, n in enumerate(nums):
            prefix_sum += n

            if prefix_sum - k in mp:
                res = max(res, i + 1 - mp[prefix_sum - k])

            if prefix_sum not in mp:
                mp[prefix_sum] = i + 1

        return res
