# Same Binary Search Tree

'''
Given two arrays representing a binary search tree, check if they are the same.

Input:
A1 = [10, 15, 8, 12, 94, 81, 5, 2, 11]
A2 = [10, 8, 5, 15, 2, 12, 11, 94, 81]

Output: True

   (GRAPH)
      10
     /  \
    8    15
   /    /  \
  5    12   94
 /    /    /
2    11   81

'''

def sameBsts(arrayOne, arrayTwo):
    return areSameBst(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))
	
def areSameBst(arr1, arr2, idx1, idx2, minVal, maxVal):
	if idx1 == -1 or idx2 == -1:
		return idx1 == idx2
	
	if arr1[idx1] != arr2[idx2]:
		return False
	
	idx1Left = getFirstSmallIdx(arr1, idx1, minVal)
	idx2Left = getFirstSmallIdx(arr2, idx2, minVal)
	idx1Right = getFirstLargeIdx(arr1, idx1, maxVal)
	idx2Right = getFirstLargeIdx(arr2, idx2, maxVal)
	
	currVal = arr1[idx1]
	leftCheck = areSameBst(arr1, arr2, idx1Left, idx2Left, minVal, currVal)
	rightCheck = areSameBst(arr1, arr2, idx1Right, idx2Right, currVal, maxVal)
	
	return leftCheck and rightCheck
	
def getFirstSmallIdx(array, idx, minVal):
	
	for i in range(idx + 1, len(array)):
		if array[i] < array[idx] and array[i] >= minVal:
			return i
	
	return -1

def getFirstLargeIdx(array, idx, maxVal):
	
	for i in range(idx + 1, len(array)):
		if array[i] > array[idx] and array[i] <= maxVal:
			return i
	
	return -1