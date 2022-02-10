# Square of Zeroes

'''
Given a square matrix nxn, return True if there exist a square which borders are all zeroes

Input:
M = [
[1 1 1 0 1 0],
[0 0 0 0 0 1],
[0 1 1 1 0 1],
[0 0 0 1 0 1],
[0 1 1 1 0 1],
[0 0 0 0 0 1]]

Output:
True
'''
# O(n^3) time | O(n^2) space
def squareOfZeroes(matrix):
    info = precompute(matrix)
	n = len(matrix)
	
	for r in range(n):
		for c in range(n):
			sqlen = 2
			
			while sqlen <= n - r and sqlen <= n - c:
				r2 = r + sqlen - 1
				c2 = c + sqlen - 1
				if isSquare(info, r, c, r2, c2):
					return True
				sqlen += 1
	
	return False

def isSquare(info, r1, c1, r2, c2):
	sqlen = c2 - c1 + 1
	
	checkTop = info[r1][c1]["zright"] >= sqlen
	checkLeft = info[r1][c1]["zbelow"] >= sqlen
	checkBot = info[r2][c1]["zright"] >= sqlen
	checkRight = info[r1][c2]["zbelow"] >= sqlen
	
	return checkTop and checkLeft and checkBot and checkRight

def precompute(M):
	info = [[x for x in row] for row in M]
	n = len(M)
	
	for i in range(n):
		for j in range(n):
			initVal = 1 if M[i][j] == 0 else 0
			info[i][j] = {"zbelow": initVal, "zright": initVal}
		
	for r in reversed(range(n)):
		for c in reversed(range(n)):
			if M[r][c] == 1:
				continue
			
			if r < n - 1:
				info[r][c]["zbelow"] += info[r+1][c]["zbelow"]

			if c < n - 1:
				info[r][c]["zright"] += info[r][c+1]["zright"]
	
	return info




'''
Recursive Solution
'''
# O(n^4) time | O(n^3) space
def squareOfZeroes(matrix):
    lastIdx = len(matrix) - 1
	
	return hasSquareOfZeroes(0, 0, lastIdx, lastIdx, matrix, {})

def hasSquareOfZeroes(r1, c1, r2, c2, matrix, cache):
	if r1 >= r2 or c1 == c2:
		return False
	
	if (r1,c1,r2,c2) in cache:
		return cache[(r1,c1,r2,c2)]
	
	flag = False
	flag |= isSquareOfZeroes(r1, c1, r2, c2, matrix)
	flag |= hasSquareOfZeroes(r1 + 1, c1, r2, c2 - 1, matrix, cache)
	flag |= hasSquareOfZeroes(r1, c1 + 1, r2 - 1, c2, matrix, cache)
	flag |= hasSquareOfZeroes(r1 + 1, c1 + 1, r2 - 1, c2 - 1, matrix, cache)
	flag |= hasSquareOfZeroes(r1 + 1, c1 + 1, r2, c2, matrix, cache)
	flag |= hasSquareOfZeroes(r1, c1, r2 - 1, c2 - 1, matrix, cache)
	
	cache[(r1,c1,r2,c2)] = flag
	return flag

def isSquareOfZeroes(r1, c1, r2, c2, matrix):
	
	for i in range(r1, r2 + 1):
		if matrix[i][c1] != 0 or matrix[i][c2] != 0:
			return False
	
	for i in range(c1, c2 + 1):
		if matrix[r1][i] != 0 or matrix[r2][i] != 0:
			return False
	
	return True