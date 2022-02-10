class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        firstParentIdx = (len(array) - 2) // 2
		
		for currentIdx in reversed(range(firstParentIdx + 1)):
			self.siftDown(currentIdx, len(array) - 1, array)
		
		return array

    def siftDown(self, currIdx, endIdx, heap):
        childOneIdx = currIdx * 2 + 1
		
		while childOneIdx <= endIdx:
			childTwoIdx = currIdx * 2 + 2 if currIdx * 2 + 2 <= endIdx else -1
			
			# pick the smallest child
			if childTwoIdx != -1 and heap[childTwoIdx] < heap[childOneIdx]:
				idxToSwap = childTwoIdx
			else:
				idxToSwap = childOneIdx
				
			# sift (swap) if child is smaller than current (parent), else return
			if heap[idxToSwap] < heap[currIdx]:
				self.swap(currIdx, idxToSwap, heap)
				currIdx = idxToSwap
				childOneIdx = currIdx * 2 + 1
			else:
				return
		
    def siftUp(self, currIdx, heap):
        parentIdx = (currIdx - 1) // 2 # get parent index
		
		# iterate through parent node and swap if parent node is bigger than child node
		while currIdx > 0 and heap[currIdx] < heap[parentIdx]:
			self.swap(currIdx, parentIdx, heap)
			currIdx = parentIdx
			parentIdx = (currIdx - 1) // 2

    def peek(self):
        return self.heap[0]

    def remove(self):
		# swap first and last element and pop the last element (smallest value). Then sift down the first value
		self.swap(0, len(self.heap) - 1, self.heap)
		valueToRemove = self.heap.pop()
		self.siftDown(0, len(self.heap) - 1, self.heap)
		return valueToRemove
	
    def insert(self, value):
        self.heap.append(value)
		self.siftUp(len(self.heap) - 1, self.heap)
	
	def swap(self, i, j, heap):
		heap[i], heap[j] = heap[j], heap[i]