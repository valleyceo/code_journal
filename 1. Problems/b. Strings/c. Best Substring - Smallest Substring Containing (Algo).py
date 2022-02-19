# Smallest Substring Containing

'''
Given two non-empty strings, one big and one small, return the smallest substring of the big string that contains all letters in the small string.

Input:
bigString = "abcd$ef$axb$c$"
smallString = "$$abf"

Output:
"f$axb$"
'''

from collections import defaultdict

# O(b + s) time | O(b + s) space
# b is length of big string and s is length of small string.
def smallestSubstringContaining(bigString, smallString):
    
	targetCounts = getCharCounts(smallString)
	minBound = findMinBound(bigString, targetCounts)
	return bigString[minBound[0]: minBound[1] + 1] if minBound[1] != float("inf") else ""

def findMinBound(string, tdict):
	minBound = [0, float("inf")]
	subdict = defaultdict(int)
	
	tcount = len(tdict.keys())
	subcount = 0
	head = 0
	tail = 0
	
	while tail < len(string):
		
		char = string[tail]
		
		if char not in tdict:
			tail += 1
			continue
		
		subdict[char] += 1
		
		if subdict[char] == tdict[char]:
			subcount += 1
			
		while subcount == tcount and head <= tail:
			minBound = getSmallerBound(head, tail, minBound[0], minBound[1])
			headChar = string[head]
			
			if headChar not in tdict:
				head += 1
				continue
			
			if subdict[headChar] == tdict[headChar]:
				subcount -= 1
			
			subdict[headChar] -= 1
			head += 1
		
		tail += 1
		
	return minBound

def getSmallerBound(idx1, idx2, idx3, idx4):
	return [idx1, idx2] if idx2 - idx1 < idx4 - idx3 else [idx3, idx4]
	
def getCharCounts(string):
	charCounts = defaultdict(int)
	
	for char in string:
		charCounts[char] += 1
		
	return charCounts
