#  LC 198. House Robber

'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
'''

# my solution
class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.bottomUp(nums)

    def topDown(self, nums: List[int]) -> int:
        @lru_cache(None)
        def solve(i):
            if i == 0:
                return nums[0]
            elif i == 1:
                return max(nums[0], nums[1])

            return max(solve(i-1), solve(i-2) + nums[i])

        return solve(len(nums)-1)

    def bottomUp(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])

        return dp[-1]

    def optimizedSolution(self, nums: List[int]) -> int:
        curr = 0
        prev = 0

        for n in arr:
            temp = curr
            curr = max(curr, prev + n)
            prev = temp

        return curr
