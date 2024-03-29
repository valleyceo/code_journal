# LC 300. Longest Increasing Subsequence

'''
Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.

Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.bottomUp(nums)
    
    # O(N^2) time | O(N) space
    def bottomUp(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)

    # Optimized: O(NlogN) time | O(N) space
    def binarySearch(self, nums: List[int]) -> int:
        sub = []
        
        for n in nums:
            i = bisect_left(sub, n)
            
            if i == len(sub):
                sub.append(n) # new max length found
            else:
                sub[i] = n
                
        return len(sub)