# Longest Increasing Subsequence
"""
Resources:
- https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
"""

# Dynamic Programming
# O(N^2) time | O(N) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
        return max(dp)

# Binary Search
# O(N*logN) time | O(1) space
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            if len(sub) == 0 or sub[-1] < x:
                sub.append(x)
            else:
                idx = bisect_left(sub, x)  # Find the index of the smallest number >= x
                sub[idx] = x  # Replace that number with x
        return len(sub)

    # For finding longest path
    def pathOfLIS(self, nums: List[int]):
        sub = []
        subIndex = []  # Store index instead of value for tracing path purpose
        path = [-1] * len(nums)  # path[i] point to the index of previous number in LIS
        for i, x in enumerate(nums):
            if len(sub) == 0 or sub[-1] < x:
                path[i] = -1 if len(subIndex) == 0 else subIndex[-1]
                sub.append(x)
                subIndex.append(i)
            else:
                idx = bisect_left(sub, x)  # Find the index of the smallest number >= x, replace that number with x
                path[i] = -1 if idx == 0 else subIndex[idx - 1]
                sub[idx] = x
                subIndex[idx] = i

        ans = []
        t = subIndex[-1]
        while t >= 0:
            ans.append(nums[t])
            t = path[t]
        return ans[::-1]

# Binary Indexed Tree
# O(N * logD) time | O(D)
# D is the different btw max and min elements
class MaxBIT:  # One-based indexing
    def __init__(self, size):
        self.bit = [0] * (size + 1)
    def get(self, idx):
        ans = 0
        while idx > 0:
            ans = max(ans, self.bit[idx])
            idx -= idx & (-idx)
        return ans
    def update(self, idx, val):
        while idx < len(self.bit):
            self.bit[idx] = max(self.bit[idx], val)
            idx += idx & (-idx)

class Solution:  # 360 ms, faster than 69.28%
    def lengthOfLIS(self, nums: List[int]) -> int:
        bit = MaxBIT(20001)
        BASE = 10001
        for x in nums:
            subLongest = bit.get(BASE + x - 1)
            bit.update(BASE + x, subLongest + 1)
        return bit.get(20001)
