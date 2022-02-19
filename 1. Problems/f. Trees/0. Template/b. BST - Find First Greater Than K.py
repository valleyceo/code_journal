# Find The First Key Greater Than Given Value in a BST

'''
- Given a BST and a value
- Find the first key that appears in an in-order traversal which is greater than the input value
'''
# O(h) time | O(1) space
def find_first_greater_than_k(tree: BstNode, k: int) -> Optional[BstNode]:

    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:  # Root and all keys in left subtree are <= k, so skip them.
            subtree = subtree.right
    return first_so_far

def find_first_greater_than_k_wrapper(tree, k):
    result = find_first_greater_than_k(tree, k)
    return result.data if result else -1
