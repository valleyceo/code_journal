# Longest String Chain

'''
You are given an array of words where each word consists of lowercase English letters.

wordA is a predecessor of wordB if and only if we can insert exactly one letter anywhere in wordA without changing the order of the other characters to make it equal to wordB.

For example, "abc" is a predecessor of "abac", while "cba" is not a predecessor of "bcad".
A word chain is a sequence of words [word1, word2, ..., wordk] with k >= 1, where word1 is a predecessor of word2, word2 is a predecessor of word3, and so on. A single word is trivially a word chain with k == 1.

Return the length of the longest possible word chain with words chosen from the given list of words.

Input:
["a","b","ba","bca","bda","bdca"]

Output:
["bdca", "bda", "ba", "a"]
'''
from collections import defaultdict

# O(nlog(n) + n*m^2) time | O(nm) space
def longestStringChain(strings):
    d = defaultdict(list)
	res = []
	sortedStrings = sorted(strings, key = len)
	
	for s in sortedStrings:
		d[s].append(s)
		
		for i in range(len(s)):
			prev = s[:i]+s[i+1:]
			
			if prev in d and len(d[prev]) >= len(d[s]):
				d[s] = [s] + d[prev]
				
				if len(d[s]) > len(res):
					res = d[s]
					
	return res