# Validate Three Nodes

'''
Given three nodes n1, n2, n3, in a binary search tree, check if there is a path n1 -> n2 -> n3 or n3 -> n2 -> n1.
'''

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    return searchNode(nodeOne, [nodeTwo, nodeThree]) or searchNode(nodeThree, [nodeTwo, nodeOne])
	
def searchNode(node, path):
	if node is None:
		return False
	
	if node.value == path[0].value:
		path.pop(0)
	
	if len(path) == 0:
		return True
	
	if node.value > path[0].value:
		return searchNode(node.left, path)
	else:
		return searchNode(node.right, path)