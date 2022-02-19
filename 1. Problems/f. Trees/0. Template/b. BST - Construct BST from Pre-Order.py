# Construct BST from Pre-Ordered Array

'''
- Given a pre-ordered array
- Reconstruct BST
- Note: a sequence <1,2,3> can have five distinct BST
'''
# O(N^2) worst case
def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:

    if not preorder_sequence:
        return None

    transition_point = next(
                            (i for i, a in enumerate(preorder_sequence) if a > preorder_sequence[0]), len(preorder_sequence))

    return BstNode(
            preorder_sequence[0],
            rebuild_bst_from_preorder(preorder_sequence[1:transition_point]),
            rebuild_bst_from_preorder(preorder_sequence[transition_point:]))


# O(N) improved alternative
def rebuild_bst_from_preorder(preorder_sequence: List[int]
                              ) -> Optional[BstNode]:
    def rebuild_bst_from_preorder_on_value_range(lower_bound, upper_bound):
        if root_idx[0] == len(preorder_sequence):
            return None

        root = preorder_sequence[root_idx[0]]

        if not lower_bound <= root <= upper_bound:
            return None

        root_idx[0] += 1

        left_subtree = rebuild_bst_from_preorder_on_value_range(lower_bound, root)
        right_subtree = rebuild_bst_from_preorder_on_value_range(root, upper_bound)
        return BstNode(root, left_subtree, right_subtree)

    root_idx = [0]
    return rebuild_bst_from_preorder_on_value_range(float('-inf'), float('-inf'))
