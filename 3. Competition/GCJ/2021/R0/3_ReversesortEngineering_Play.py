import sys
import collections
from math import factorial
import itertools
from itertools import permutations

def getNthPermutation( pIndex, inList, outList=[] ):
  """ get :pIndex: permutation of :inList:
 
  :warn: permutations are sorted in lexicographical order starting from 0, i.e.:
  0 -> [1, 2, 3], 1 -> [1, 3, 2] and so on
  :param int pIndex: given permutation index
  :param list inList: initial list of elements
  :param list outList: result list
  """
  ## permutation index too big
  if pIndex >= factorial( len(inList) ): return []
  ## no more elements to use
  if not inList: return outList
  ## make sure eList is sorted
  inList.sort()
  ## get factorial
  f = factorial( len(inList)-1 )
  index = pIndex // f
  reminder = pIndex % f
  ## add new element to outList
  outList.append( inList[index] )
  ## ...and remove it from inList
  del inList[index]
  ## bail out or call recursively depending of the reminder 
  if not reminder:
    return outList + inList
  else:
    return getNthPermutation( reminder, inList, outList )

# 1. Reversesort
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
	N = input().strip()
	L = [int(x) for x in input().strip().split(" ")]
	
	#print("Case #{}: {}".format(t, res))

print("Len, Min, Max")
for NL in range(2, 5):
	pList = [i for i in range(1, NL+1)]
	d = collections.defaultdict(int)
	maxN = -1
	minN = sys.maxsize

	for pl in list(itertools.permutations(pList)):
		
		a = ReverseSortCount(list(pl))
		maxN = max(maxN, a)
		minN = min(minN, a)
		d[a] += 1

	print(NL, minN, maxN, GetMax(NL))
	for x in range(minN, maxN + 1):
		if x not in d:
			print("{} does not exist!", x)


NL = 10 #3628800
nlist = [i for i in range(1, NL + 1)]

print(GetMax(NL))
print(factorial(len(nlist))//2)

temp = []
x = getNthPermutation(factorial(len(nlist))//2, nlist, temp)
print("hrer", x)
print(ReverseSortCount(x))
d = collections.defaultdict(int)

maxN = -1
minN = sys.maxsize

for i in range(1000):
	a = ReverseSortCount(nlist)
	maxN = max(maxN, a)
	minN = min(minN, a)

print(d, minN, maxN)



'''
Pattern search:
Len Min Max
5	4	14

'''