# Number of Binary Tree Topologies

'''
Given a non-negative integer n, return the number of possible binary tree topologies that can be created with exactly n nodes

Input:
n = 3

Output:
5
'''
# Optimal iterative solution, O(n^2) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    cache = [1]
	
	for m in range(1, n + 1):
		numOfTrees = 0
		
		for left in range(m):
			right = m - 1 - left
			numLeft = cache[left]
			numRight = cache[right]
			numOfTrees += numLeft * numRight
			
		cache.append(numOfTrees)
	
	return cache[-1]

# Recursive solution (can use cache)
# Upper bound: O(n*(2n)!/(n!(n+1)!)) time | O(n) space
def numberOfBinaryTreeTopologies(n):
    return getNumbers(n)

def getNumbers(n):
	if n == 0:
		return 1
		
	total = 0
	for i in range(n):
		left = getNumbers(i)
		right = getNumbers(n - i - 1)
		total += left * right
		
	return total