# Optimal O(nlog(n)) time | O(n) space
def mergeSort(array):
    if len(array) <= 1:
		return array
	
	copy = array[:]
	mergeHelper(array, 0, len(array) - 1, copy)
	return array

def mergeHelper(main, startIdx, endIdx, copy):
	if startIdx == endIdx:
		return
	
	middleIdx = (startIdx + endIdx) // 2
	# main will be sorted, so you need to copy the sorted main array to the copy array. Instead of copying you can just swap the two and use the unsorted "copy" array as the next main array
	mergeHelper(copy, startIdx, middleIdx, main) 
	mergeHelper(copy, middleIdx + 1, endIdx, main)
	merge(main, startIdx, middleIdx, endIdx, copy)

def merge(main, startIdx, middleIdx, endIdx, copy):
	k = startIdx
	i = startIdx
	j = middleIdx + 1
	
	while i <= middleIdx and j <= endIdx:
		if copy[i] <= copy[j]:
			main[k] = copy[i]
			i += 1
		else:
			main[k] = copy[j]
			j += 1
		
		k += 1
	
	while i <= middleIdx:
		main[k] = copy[i]
		i += 1
		k += 1
		
	while j <= endIdx:
		main[k] = copy[j]
		j += 1
		k += 1


'''
Easy solution
'''
# O(nlog(n)) time | O(nlog(n)) space
def mergeSort(array):
    if len(array) == 1:
		return array
	
	midIdx = len(array) // 2
	leftArr = mergeSort(array[:midIdx])
	rightArr = mergeSort(array[midIdx:])
	
	return mergeArrays(leftArr, rightArr)
	
def mergeArrays(array1, array2):
	idx1 = 0
	idx2 = 0
	newArr = []
	
	while idx1 < len(array1) and idx2 < len(array2):
		if array1[idx1] <= array2[idx2]:
			newArr.append(array1[idx1])
			idx1 += 1
		else:
			newArr.append(array2[idx2])
			idx2 += 1
			
	while idx1 < len(array1):
		newArr.append(array1[idx1])
		idx1 += 1
		
	while idx2 < len(array2):
		newArr.append(array2[idx2])
		idx2 += 1
	
	return newArr