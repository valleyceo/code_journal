# Binary Tree Implementation
class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()
