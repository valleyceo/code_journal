import sys
import collections
from math import factorial
import itertools
from itertools import permutations

def findMaxIndex(index,a,curr):
	ans = -1
	index = 0
	for i in range(index,len(a)):
		if a[i]>curr:
			if ans == -1:
				ans = curr
				index = i
			else:
				ans = min(ans,a[i])
				index = i
	return index

def nextPerm(nums):
	found = False
	i = len(nums)-2
	while i >=0:
		if nums[i] < nums[i+1]:
			found =True
			break
		i-=1
	if not found:
		nums.sort()
	else:
		m = findMaxIndex(i+1,nums,nums[i])
		nums[i],nums[m] = nums[m],nums[i]
		nums[i+1:] = nums[i+1:][::-1]
	return nums

def GetMinIndex(n: int, L: list):
	minVal = sys.maxsize
	minIdx = -1

	for i in range(n, len(L)):
		if L[i] < minVal:
			minVal = L[i]
			minIdx = i

	return minIdx

def ReverseSortCount(LL: list):
	L = LL.copy()
	res = 0

	for i in range(len(L)-1):
		minIdx = GetMinIndex(i, L)
		
		endIdx = min(minIdx+1, len(L))
		if (endIdx > i):
			L[i:endIdx] = reversed(L[i:endIdx])
		res += endIdx - i

	return res

def GetMax(n: int):
	if n == 2:
		return 2

	res = 2
	x = 3

	for i in range(3, n+1):
		res += x
		x += 1

	return res

T = int(input())

for t in range(1, T + 1):
	(N, C) = input().strip().split(" ")
	N = int(N)
	C = int(C)

	nlist = [i for i in range(1, N + 1)]

	if C < N-1 or C > GetMax(N):
		print("Case #{}: IMPOSSIBLE".format(t))
		continue

	if C == N-1:
		print("Case #{}: ".format(t) + " ".join(map(str, nlist)))
		continue

	for i in range(1, factorial(len(nlist))):
		nlist = nextPerm(nlist)
		a = ReverseSortCount(nlist)

		if a == C:
			print("Case #{}: ".format(t) + " ".join(map(str, nlist)))
			break