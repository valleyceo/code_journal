# Find Root to Leaf Path with Specified Sum

'''
- Given a binary tree and an integer value
- Return if there exist a path to node where the sum equals to the desired value
'''
# O(n) time | O(h) space
def has_path_sum(tree: BinaryTreeNode, remaining_weight: int) -> bool:

    if not tree:
        return False
    if not tree.left and not tree.right:  # Leaf.
        return remaining_weight == tree.data
    # Non-leaf.
    return (has_path_sum(tree.left, remaining_weight - tree.data)
            or has_path_sum(tree.right, remaining_weight - tree.data))
