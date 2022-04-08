# Reverse Sort
import sys

def GetMinIndex(n: int, L: list):
	minVal = sys.maxsize
	minIdx = -1

	for i in range(n, len(L)):
		if L[i] < minVal:
			minVal = L[i]
			minIdx = i

	return minIdx

T = int(input())

for t in range(1, T + 1):
	N = input().strip()
	L = [int(x) for x in input().strip().split(" ")]
	res = 0

	for i in range(len(L)-1):
		minIdx = GetMinIndex(i, L)

		endIdx = min(minIdx+1, len(L))
		if (endIdx > i):
			L[i:endIdx] = reversed(L[i:endIdx])
		res += endIdx - i

	print("Case #{}: {}".format(t, res))
