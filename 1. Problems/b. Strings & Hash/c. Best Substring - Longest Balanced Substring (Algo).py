# Longest Balanced Substring

'''
Given a string of paranthesis "(" and ")", return the longest length of substring that is valid.

Input:
string = "(()))("

Output:
4 # Longest is "(())"
'''
# O(n) time | O(1) space
def longestBalancedSubstring(string):
    
	return max(getLongestByDirection(string, True),
			  getLongestByDirection(string, False))

def getLongestByDirection(string, startLeft):
	openChar = "(" if startLeft else ")"
	idx = 0 if startLeft else len(string) - 1
	step = 1 if startLeft else -1
	maxLen = 0
	
	openCount = 0
	closeCount = 0
	
	while idx >= 0 and idx < len(string):
		if string[idx] == openChar:
			openCount += 1
		else:
			closeCount += 1

		if openCount == closeCount:
			maxLen = max(maxLen, closeCount * 2)
		elif openCount < closeCount:
			openCount = 0
			closeCount = 0
		
		idx += step
		
	return maxLen

'''
Brute force solution
'''
# O(n^3) time | O(n) space
def longestBalancedSubstring(string):
    maxLength = 0
	
	for i in range(len(string)):
		for j in range(i + 2, len(string) + 1, 2):
			if isBalanced(string[i:j]):
				currentLength = j - i
				maxLength = max(maxLength, currentLength)
	
	return maxLength

def isBalanced(string):
	stack = []
	
	for char in string:
		if char == "(":
			stack.append("(")
		elif len(stack) > 0:
			stack.pop()
		else:
			return False
	
	return len(stack) == 0