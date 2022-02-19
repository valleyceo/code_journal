# Find the K Largest Element in BST

'''
- Given a BST and an integer K
- Return the k largest elements in the BST in decreasing order
'''

# O(h + k) time
def find_k_largest_in_bst(tree: BstNode, k: int) -> List[int]:
    def find_k_largest_in_bst_helper(tree):
        # Perform reverse inorder traversal.
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements: List[int] = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements
