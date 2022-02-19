# Form a Linked List from the Leaves of a Binary Tree

'''
- Given a binary tree
- Compute linked list from the leaves of binary tree (in left-to-right order)
'''

# O(n) time
def create_list_of_leaves(tree: BinaryTreeNode) -> List[BinaryTreeNode]:

    if not tree:
        return []
    if not tree.left and not tree.right:
        return [tree]
    # First do the left subtree, and then do the right subtree.
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)
