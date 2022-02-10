# Palindrome Partitioning Min Cuts

'''
Given a string, return minimum number of cuts to create strings of palindromes

Input:
"noonabbad"

Output:
2 # noon | abba | d
'''
# O(n^2) time | O(n^2) space
def Solution2(string):
    dp = [[False for _ in string] for _ in string]
	
	for i in range(len(string)):
		dp[i][i] = True
	
	for length in range(2, len(string) + 1):
		for i in range(0, len(string) - length + 1):
			j = i + length - 1
			
			if length == 2:
				dp[i][j] = string[i] == string[j]
			else:
				dp[i][j] = string[i] == string[j] and dp[i+1][j-1]
	
	cuts = [float("inf") for i in string]
	
	for i in range(len(string)):
		if dp[0][i]:
			cuts[i] = 0
		else:
			cuts[i] = cuts[i - 1] + 1
			for j in range(1, i):
				if dp[j][i]:
					cuts[i] = min(cuts[i], cuts[j - 1] + 1)
	
	return cuts[-1]
			
def isPalindrome(string):
	left = 0
	right = len(string) - 1
	
	while left < right:
		if string[left] != string[right]:
			return False
		
		left += 1
		right -= 1
	
	return True

# O(n^3) time, O(n^2) space
def Solution1(string):
    dp = [[False for _ in string] for _ in string]
	
	for i in range(len(string)):
		for j in range(i, len(string)):
			dp[i][j] = isPalindrome(string[i : j + 1])
	
	cuts = [float("inf") for i in string]
	
	for i in range(len(string)):
		if dp[0][i]:
			cuts[i] = 0
		else:
			cuts[i] = cuts[i - 1] + 1
			for j in range(1, i):
				if dp[j][i]:
					cuts[i] = min(cuts[i], cuts[j - 1] + 1)
	
	return cuts[-1]
			
def isPalindrome(string):
	left = 0
	right = len(string) - 1
	
	while left < right:
		if string[left] != string[right]:
			return False
		
		left += 1
		right -= 1
	
	return True