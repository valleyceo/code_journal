# Right Smaller than

'''
Given an array of integers, return the count of smaller values on the right for each position

Input:
[8, 5, 11, -1, 3, 4, 2]

Output:
[5, 4, 4, 0, 1, 1, 0]
'''
def rightSmallerThan(array):
    bst = SBST()
	return bst.getRST(array)

class SBST:
	def __init__(self):
		self.root = None
	
	def getRST(self, nums):
		rst = []
		
		for n in reversed(nums):
			rst.append(self.add(n))
			
		return rst[::-1]
	
	def add(self, n):
		if self.root is None:
			self.root = Node(n)
			return 0
		
		rs = 0
		curr = self.root
		
		while curr:
			if n <= curr.val:
				curr.countLeft += 1
				
				if curr.left is None:
					curr.left = Node(n)
					return rs
				
				curr = curr.left
			else:
				rs += curr.countLeft + 1
				
				if curr.right is None:
					curr.right = Node(n)
					return rs
				
				curr = curr.right
		
		return rs
		
class Node:
	def __init__(self, n):
		self.val = n
		self.left = None
		self.right = None
		self.countLeft = 0