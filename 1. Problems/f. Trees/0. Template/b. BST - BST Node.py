# BST Node

'''
- Similar to sorted arrays, but efficient in adding and deleting elements
- Look up time of O(logn)
- Avoid mutating objects in BST, always first remove from tree then add
- Search time complexity: O(h)
'''
class BstNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

    def __eq__(self, other):
        return equal_binary_trees(self, other)

    def __repr__(self):
        return str(binary_tree_to_string(self))

    def __str__(self):
        return self.__repr__()

# O(h) search time complexity
def search_bst(tree: BstNode, key: int) -> Optional[BstNode]:
    return (tree if not tree or tree.data == key else search_bst(
        tree.left, key) if key < tree.data else search_bst(tree.right, key))
