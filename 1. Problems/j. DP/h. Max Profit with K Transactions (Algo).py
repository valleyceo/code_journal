# Max Profit with K Transactions

"""
You are given an array of integers representing the prices of a single stock on various days (each index in the array represents a different day). You are also given an integer k, which represents the number of transactions you are allowed to make. One transaction consists of buying the stock on a given day and selling it on another, later day.

Write a function that returns the maximum prot that you can make buying and selling the stock, given k transactions.

Note that you can only hold 1 share of the stock at a time; in other words, you cannot buy more than 1 share of the stock on any given day, and you cannot buy a share of the stock if you are still holding another share.

Sample input:
prices = [5, 11, 3, 50, 60, 90]
k = 2

Sample output:
93 // Buy: 5, Sell: 11; Buy: 3, Sell: 90
"""

def Solution1(prices, k):
    if len(prices) == 0:
		return 0

	profits = [[0 for d in prices] for t in range(k + 1)]

	for t in range(1, k + 1):
		maxThusFar = float("-inf")

		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, profits[t-1][d-1]-prices[d-1])
			profits[t][d] = max(profits[t][d-1], maxThusFar + prices[d])

	return profits[-1][-1]


def Solution2(prices, k):
	if not len(prices):
		return 0

	evenProfits = [0 for _ in prices]
	oddProfits = [0 for _ in prices]

	for t in range(1, k + 1):
		maxThusFar = float('-inf')

		if t % 2 == 1:
			currentProfits = oddProfits
			previousProfits = evenProfits
		else:
			currentProfits = evenProfits
			previousProfits = oddProfits

		for d in range(1, len(prices)):
			maxThusFar = max(maxThusFar, previousProfits[d-1] - prices[d-1])
			currentProfits[d] = max(currentProfits[d-1], maxThusFar + prices[d])

	return currentProfits[-1]
