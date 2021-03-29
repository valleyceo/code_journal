# 5. Cheating Detection

import sys
import math

SampleSize = 2500

class Solution:
	def findCheater(self, A):
		self.avg = [0.0] * 10000
		self.lowAvgList = []
		self.processAvg(A)

		self.std = [0.0] * len(self.lowAvgList)
		self.processStd(A)
		self.playerPSum = [0.0] * 100
		self.processPlayerPerformance(A)

		maxP = -1
		maxIdx = -1

		for i in range(100):
			if self.playerPSum[i] > maxP:
				maxP = self.playerPSum[i]
				maxIdx = i + 1

		return maxIdx

	def processAvg(self, A):
		for i in range(10000):
			for j in range(100):
				self.avg[i] += A[j][i]

			self.avg[i] /= 100

		self.lowAvgList = sorted(range(len(self.avg)), key=lambda k: self.avg[k])[:SampleSize]

	def processStd(self, A):
		for i in range(len(self.lowAvgList)):
			idx = self.lowAvgList[i]
			for j in range(100):
				self.std[i] += (A[j][idx]-self.avg[idx]) * (A[j][idx]-self.avg[idx])

			self.std[i] = math.sqrt(self.std[i]/100)

	def processPlayerPerformance(self, A):
		for i in range(100):
			pSum = 0

			for j in range(len(self.lowAvgList)):
				idx = self.lowAvgList[j]

				if A[i][idx] == 1:
					zScore = (1 - self.avg[idx])/self.std[j]
					pScore = self.getPercentile(zScore)
					pSum += pScore
				else:
					pSum += 0.5

			self.playerPSum[i] = pSum / len(self.lowAvgList)

	def getPercentile(self, z):

		if (z < -6.5):
		    return 0.0

		if (z > 6.5):
			return 1.0

		if (z > 0):
			z = -z

		factK = 1.0
		sumVal = 0.0
		term = 1.0
		k = 0.0
		loopStop = math.exp(-1.0)

		while abs(term) > loopStop:
			term = .3989 * (-1**k) * (z**k) / (2 * k + 1) / (2**k) * (z**(k+1)) / factK
			sumVal += term
			k += 1
			factK *= k

		sumVal += 0.5
		return min(sumVal, 1.0)

T = int(input())
P = int(input())

for t in range(1, T + 1):
	Answers = []
	mySolution = Solution()

	for i in range(100):
		Answers.append([float(i) for i in input().strip()])

	ans = mySolution.findCheater(Answers)
	print("Case #{}: {}".format(t, ans))
