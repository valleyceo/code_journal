# Count Inversions

'''
Given an array of integers, return the number of inversions to make array sorted.

Input:
array = [2, 3, 3, 1, 9, 5, 6]

Output:
5
'''

# O(nlogn) time | O(n) space
def countInversions(array):
    # Write your code here.
    return mergeSortCount(0, len(array), array)

def mergeSortCount(start, end, array):
	if end - start <= 1:
		return 0
	
	mid = (start + end) // 2
	leftCount = mergeSortCount(start, mid, array)
	rightCount = mergeSortCount(mid, end, array)
	mergeCount = mergeArrayCount(start, mid, end, array)
	
	return leftCount + rightCount + mergeCount

def mergeArrayCount(start, middle, end, array):
	idx1 = start
	idx2 = middle
	count = 0
	merged = []
	
	while idx1 < middle and idx2 < end:
		if array[idx1] <= array[idx2]:
			merged.append(array[idx1])
			idx1 += 1
		else:
			merged.append(array[idx2])
			idx2 += 1
			count += middle - idx1
			
	merged += array[idx1:middle] + array[idx2:end]
	
	for idx, num in enumerate(merged):
		array[start + idx] = num
	
	return count
		