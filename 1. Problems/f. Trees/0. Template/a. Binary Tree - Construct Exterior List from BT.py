# Compute the Exterior of Number of Nodes

'''
- Exterior represents the sequence of left-most nodes, all bottom leaf-nodes, right-most nodes in a counter-clockwise order.
'''

# O(n) time
def exterior_binary_tree(tree: BinaryTreeNode) -> List[BinaryTreeNode]:

    # Computes the nodes from the root to the leftmost leaf.
    def left_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        exterior.append(subtree)
        if subtree.left:
            left_boundary(subtree.left)
        else:
            left_boundary(subtree.right)

    # Computes the nodes from the rightmost leaf to the root.
    def right_boundary(subtree):
        if not subtree or (not subtree.left and not subtree.right):
            return
        if subtree.right:
            right_boundary(subtree.right)
        else:
            right_boundary(subtree.left)
        exterior.append(subtree)

    # Compute the leaves in left-to-right order.
    def leaves(subtree):
        if not subtree:
            return
        if not subtree.left and not subtree.right:
            exterior.append(subtree)
            return
        leaves(subtree.left)
        leaves(subtree.right)

    if not tree:
        return []

    exterior = [tree]
    left_boundary(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_boundary(tree.right)
    return exterior
