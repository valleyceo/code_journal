# LC 312. Burst Balloons

'''
You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.

If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

Return the maximum coins you can collect by bursting the balloons wisely.

Example 1:

Input: nums = [3,1,5,8]
Output: 167
Explanation:
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
'''

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        return self.bottomUp(nums)

    # O(N^3) time | O(N^2) space
    def topDown(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]

        @lru_cache(None)
        def dp(left, right):

            if right < left:
                return 0

            res = 0

            for i in range(left, right + 1):
                val = nums[left - 1] * nums[i] * nums[right + 1]
                rem = dp(left, i - 1) + dp(i + 1, right)

                res = max(res, val + rem)

            return res

        return dp(1, len(nums) - 2)

    # O(N^3) time | O(N^2) space
    def bottomUp(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for left in range(n - 2, 0, -1):
            for right in range(left, n - 1):

                for i in range(left, right + 1):
                    val = nums[left - 1] * nums[i] * nums[right + 1]
                    rem = dp[left][i - 1] + dp[i + 1][right]
                    dp[left][right] = max(dp[left][right], val + rem)

        return dp[1][-2]

"""
Note:
- Think backwards: think you are adding balloons from empty
"""
