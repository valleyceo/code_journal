# 2. Moons and Umbrellas

import sys

class Solution:
	def search(self, X: int, Y: int, S: list):

		for i in range(len(S)):
			if S[i] != "?":
				expanded = self.expand(i, S)

		if S[0] == "?":
			return 0
		else:
			return self.computeVal(X, Y, S)

	def expand(self, idx: int, S: list):
		if S[idx] == "?":
			print("ERROR")
			return

		for i in range(idx + 1, len(S)):
			if S[i] == "?":
				S[i] = S[idx]
			else:
				break

		for i in range(idx - 1, -1, -1):
			if S[i] == "?":
				S[i] = S[idx]
			else:
				break

	def computeVal(self, X: int, Y: int, S: str):
		val = 0

		for i in range(1, len(S)):
			if S[i-1] == "C" and S[i] == "J":
				val += X
			elif S[i-1] == "J" and S[i] == "C":
				val += Y

		return val

T = int(input())

for t in range(1, T + 1):
	(X, Y, S) = input().strip().split(" ")
	X = int(X)
	Y = int(Y)
	S = list(S)
	mySolution = Solution()
	ans = mySolution.search(X, Y, S)

	print("Case #{}: {}".format(t, ans))




