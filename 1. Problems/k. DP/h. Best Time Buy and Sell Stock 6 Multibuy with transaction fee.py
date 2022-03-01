# LC 714. Best Time Buy and Sell Stock VI

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:

Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

Example 2:

Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

Constraints:

1 <= prices.length <= 5 * 104
1 <= prices[i] < 5 * 104
0 <= fee < 5 * 104
'''
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        return self.optimal(prices, fee)
        
    def optimal(self, prices: List[int], fee: int) -> int:
        buy = -prices[0] - fee
        sell = 0
        
        for i in range(1, len(prices)):
            prev_buy = buy
            buy = max(buy, sell - prices[i] - fee)
            sell = max(sell, prev_buy + prices[i])
            
        return sell
    
    
    def explanation(self, prices: List[int], fee: int) -> int:
        
        if len(prices) == 1:
            return 0
        
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0] - fee
        
        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i] - fee) # max(do nothing, buy)
            sell[i] = max(sell[i-1], buy[i-1] + prices[i]) # max(do nothing, sell)
        
        return sell[-1]