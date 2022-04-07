# LC 377. Combination Sum IV

'''
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.

Example 2:

Input: nums = [9], target = 3
Output: 0
'''
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        return self.bottomUp(nums, target)

    # O(T * N) time | O(T) space
    def topDown(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize = None)
        def helper(rem):
            if rem == 0:
                return 1

            res = 0

            for n in nums:
                if rem >= n:
                    res += helper(rem - n)

            return res

        return helper(target)

    # O(T * N) time | O(T) space
    def bottomUp(self, nums: List[int], target: int) -> int:
        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for comb_val in range(target + 1):
            for n in nums:
                if comb_val >= n:
                    dp[comb_val] += dp[comb_val - n]

        return dp[-1]
