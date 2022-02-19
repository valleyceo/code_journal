# Compare Leaf Traversal

'''
Given two binary trees, check if leaf nodes sequence (In-Order) are the same

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
'''
# Optimized Link (tree mutation) solution: O(n + m) time, O(max(h1, h2)) space
def Solution2(tree1, tree2):
    t1head, _ = connectLeafs(tree1)
	t2head, _ = connectLeafs(tree2)
	
	while t1head and t2head:
		if t1head.value != t2head.value:
			return False
		
		t1head = t1head.right
		t2head = t2head.right
	
	return t1head is None and t2head is None
	
def connectLeafs(curr, head = None, prev = None):
	if curr is None:
		return head, prev
	
	if isLeaf(curr):
		if prev is None:
			head = curr
		else:
			prev.right = curr
		
		prev = curr
	
	leftHead, leftPrev = connectLeafs(curr.left, head, prev)
	return connectLeafs(curr.right, leftHead, leftPrev)

# Stack Solution: O(n + m) time, O(h1 + h2) space
def Solution1(tree1, tree2):
    stack1 = [tree1]
	stack2 = [tree2]
	
	while stack1 and stack2:
		nextLeaf1 = getNextLeafNode(stack1)
		nextLeaf2 = getNextLeafNode(stack2)
		
		if nextLeaf1.value != nextLeaf2.value:
			return False
	
	return len(stack1) == 0 and len(stack2) == 0

def getNextLeafNode(traversalStack):
	currentNode = traversalStack.pop()
	
	while not isLeafNode(currentNode):
		if currentNode.right is not None:
			traversalStack.append(currentNode.right)
		
		if currentNode.left is not None:
			traversalStack.append(currentNode.left)
		
		currentNode = traversalStack.pop()
	
	return currentNode

def isLeafNode(node):
	return node.left is None and node.right is None