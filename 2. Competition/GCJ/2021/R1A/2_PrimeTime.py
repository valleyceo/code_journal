# 2. Prime Time
# NOTE: Passes up to Test Set 2

import sys

class Solution:

	def FindMax(self, l, s):
		self.max = -1
		self.search(0, l, 1, s)
		return self.max if (self.max > 0) else 0

	def search(self, idx, l, pathProd, pathSum):
		if pathProd == pathSum:
			self.max = max(self.max, pathProd)
			return

		if idx == len(l):
			return

		if pathProd > 49900:
			return

		prod = 1
		for c in range(l[idx][1] + 1):
			self.search(idx + 1, l, pathProd * prod, pathSum - (l[idx][0] * c))
			prod *= l[idx][0]

T = int(input())
obj = Solution()

for t in range(1, T + 1):
	X = int(input())
	l = []
	s = 0
	for i in range(X):
		NC = [int(x) for x in input().strip().split(" ")]
		l.append(NC)
		s += NC[0] * NC[1]

	res = obj.FindMax(l, s)
	print("Case #{}: {}".format(t, res))