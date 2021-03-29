# 2. Moons and Umbrellas

import sys

class Solution:
	def search(self, X: int, Y: int, S: list):
		self.X = X
		self.Y = Y
		self.minVal = sys.maxsize
		self.backtrack(0, S, 0)
		return self.minVal

	def backtrack(self, idx: int, pathStr: list, sumVal: int):

		if idx == len(self.S):
			if self.minVal > sumVal:
				self.minVal = min(self.minVal, sumVal)
			return

		if idx == 0:
			if pathStr[idx] == "?":
				pathStr[idx] = "C"
				self.backtrack(idx+1, pathStr, sumVal)
				pathStr[idx] = "J"
				self.backtrack(idx+1, pathStr, sumVal)
				pathStr[idx] = "?"
			else:
				self.backtrack(idx+1, pathStr, sumVal)
			return

		if pathStr[idx] == "?":
			
			pathStr[idx] = "C"
			if pathStr[idx-1] == "J":
				self.backtrack(idx+1, pathStr, sumVal + self.Y)
			else:
				self.backtrack(idx+1, pathStr, sumVal)


			pathStr[idx] = "J"
			if pathStr[idx-1] == "C":
				self.backtrack(idx+1, pathStr, sumVal + self.X)
			else:
				self.backtrack(idx+1, pathStr, sumVal)

			pathStr[idx] = "?"
		else:
			if pathStr[idx-1] == "C" and self.S[idx] == "J":
				self.backtrack(idx+1, pathStr, sumVal + self.X)
			elif self.S[idx-1] == "J" and self.S[idx] == "C":
				self.backtrack(idx+1, pathStr, sumVal + self.Y)
			else:
				self.backtrack(idx+1, pathStr, sumVal)

T = int(input())

for t in range(1, T + 1):
	(X, Y, S) = input().strip().split(" ")
	X = int(X)
	Y = int(Y)
	S = list(S)
	mySolution = Solution()
	ans = mySolution.search(X, Y, S)

	print("Case #{}: {}".format(t, ans))




