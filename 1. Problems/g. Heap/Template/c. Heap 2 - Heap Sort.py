# Heap Sort - O(nlogn) time complexity, O(1) space complexity
def heapSort(nums):
    buildHeap(nums)
	
	for i in reversed(range(1, len(nums))):
		nums[0], nums[i] = nums[i], nums[0]
		siftDown(0, i - 1, nums)
	
	return nums
	
def buildHeap(nums):
	pIdx = (len(nums) - 2) // 2 # first parent idx
	
	for i in reversed(range(pIdx + 1)):
		siftDown(i, len(nums) - 1, nums)
		
def siftDown(currIdx, endIdx, arr):
	idx1 = currIdx * 2 + 1 # first child
	idx2 = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1 # second child, -1 if it does not exist
	
	while idx1 <= endIdx:
		if idx2 != -1 and arr[idx1] < arr[idx2]:
			tempIdx = idx2
		else:
			tempIdx = idx1
		
		if arr[tempIdx] > arr[currIdx]:
			arr[tempIdx], arr[currIdx] = arr[currIdx], arr[tempIdx]
			currIdx = tempIdx
			idx1 = currIdx * 2 + 1 # first child
			idx2 = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1 # second child, -1 if it does not exist
		else:
			return