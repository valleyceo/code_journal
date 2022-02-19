# Sum Root to Leaf

'''
- Given a Binary tree with 1 and 0
- Find the sum of all binary numbers path available from root to leaves
'''

# O(n) time | O(h) space
def sum_root_to_leaf(tree: BinaryTreeNode) -> int:
    def sum_root_to_leaf_helper(tree, partial_path_sum=0):
        if not tree:
            return 0

        partial_path_sum = partial_path_sum * 2 + tree.data
        if not tree.left and not tree.right:  # Leaf.
            return partial_path_sum
        # Non-leaf.
        return (sum_root_to_leaf_helper(tree.left, partial_path_sum) +
                sum_root_to_leaf_helper(tree.right, partial_path_sum))

    return sum_root_to_leaf_helper(tree)
