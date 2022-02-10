"""
LC 494. Target Sum

You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
 

Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        self.dp = [[-sys.maxsize]*2000 for i in range(len(nums))]
        self.sum = S
        self.found = 0
        self.nums = nums
        self.len = len(nums)
        
        return self.permute(0, 0)
    
    def permute(self, idx: int, n: int):
        
        if (idx == self.len):
            if n == self.sum:
                return 1
            else:
                return 0
        
        if (self.dp[idx][n + 1000] != -sys.maxsize):
            return self.dp[idx][n + 1000]
        
        add = self.permute(idx + 1, n + self.nums[idx])
        subtract = self.permute(idx + 1, n - self.nums[idx])