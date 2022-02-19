# Find the LCA in BST

'''
- Given a BST and two nodes
- Return the LCA of the two nodes
'''

# O(h) time | O(1) space
def find_lca(tree: BstNode, s: BstNode, b: BstNode) -> Optional[BstNode]:

    while tree.data < s.data or tree.data > b.data:
        # Keep searching since tree is outside of [s, b].
        while tree.data < s.data:
            tree = tree.right  # LCA must be in tree's right child.
        while tree.data > b.data:
            tree = tree.left  # LCA must be in tree's left child.
    # Now, s.data <= tree.data && tree.data <= b.data.
    return tree
