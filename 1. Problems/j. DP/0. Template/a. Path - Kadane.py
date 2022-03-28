# Kadane Algorithm

'''
Problem: Given an array of values, return the subarray with largest sum
'''

def kadane(nums):
    pathSum = 0
	maxSum = float('-inf')

	for n in nums:
		pathSum = max(pathSum + n, n)
		maxSum = max(maxSum, pathSum)

	return maxSum
