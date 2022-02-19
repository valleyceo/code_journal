# LCS Return Longest String

# O(m*n*min(m,n)) time and space
def solution1(str1, str2):
    dp = [[[] for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
	
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i-1] == str1[j-1]:
				dp[i][j] = dp[i-1][j-1] + [str2[i-1]]
			else:
				dp[i][j] = max(dp[i-1][j], dp[i][j-1], key = len)
	
	return dp[-1][-1]

# O(mn) time, O(mn) space
def solution2(str1, str2):
	#	  [string, len, idx1, idx2]
    dp = [[[None, 0, None, None] for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
	
	for i in range(1, len(str2) + 1):
		for j in range(1, len(str1) + 1):
			if str2[i - 1] == str1[j - 1]:
				dp[i][j] = [str2[i - 1], dp[i - 1][j - 1][1] + 1, i - 1, j - 1]
			else:
				if dp[i - 1][j][1] > dp[i][j - 1][1]:
	 				dp[i][j] = [None, dp[i - 1][j][1], i - 1, j]
				else:
					dp[i][j] = [None, dp[i][j - 1][1], i, j - 1]
	return buildSeq(dp)
	
def buildSeq(dp):
	seq = []
	i = len(dp) - 1
	j = len(dp[0]) - 1
	
	while i != 0 and j != 0:
		curr = dp[i][j]
		
		if curr[0] is not None:
			seq.append(curr[0])
		i = curr[2]
		j = curr[3]
		
	return list(reversed(seq))