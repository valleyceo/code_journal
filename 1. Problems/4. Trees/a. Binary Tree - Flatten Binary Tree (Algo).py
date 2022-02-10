# Flatten Binary Tree

'''
Given a binary tree, flatten into a linked list in In-Order

class BinaryTree:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
'''
def flattenBinaryTree(root):
    return flattenTree(root)[0]
	
def flattenTree(node):
	
	if node.left is None:
		leftMost = node
	else:
		leftSubtreeLeftMost, leftSubtreeRightMost = flattenTree(node.left)
		connect(leftSubtreeRightMost, node)
		leftMost = leftSubtreeLeftMost
		
	if node.right is None:
		rightMost = node
	else:
		rightSubtreeLeftMost, rightSubtreeRightMost = flattenTree(node.right)
		connect(node, rightSubtreeLeftMost)
		rightMost = rightSubtreeRightMost
	
	return [leftMost, rightMost]

def connect(left, right):
	left.right = right
	right.left = left