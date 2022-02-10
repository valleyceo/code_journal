# LC 746. Min Cost Climbing Stairs

'''
You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
 
Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
'''

# my solution - optimal
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return self.dpConstant(cost)
    
    def dpConstant(self, cost: List[int]) -> int:
        first = 0
        second = 0
        
        for i in range(2, len(cost)+1):
            temp = first
            first = min(first+cost[i-1], second+cost[i-2])
            second = temp
        
        return first
        
    def dp(self, cost: List[int]) -> int:
        dp = [sys.maxsize] * (len(cost) + 2)
        dp[0] = 0
        dp[1] = 0
        
        for i in range(len(cost)):
            dp[i + 1] = min(dp[i + 1], dp[i] + cost[i])
            dp[i + 2] = min(dp[i + 2], dp[i] + cost[i])
        
        return dp[len(cost)]