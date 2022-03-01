# Compute the LCA, Optimizing for Close Ancestors

# O(h) time | O(1) space
def lca(node0: BinaryTreeNode,
        node1: BinaryTreeNode) -> Optional[BinaryTreeNode]:

    iter0, iter1 = node0, node1
    nodes_on_path_to_root: Set[BinaryTreeNode] = set()

    while iter0 or iter1:
        # Ascend tree in tandem for these two nodes.
        if iter0:
            if iter0 in nodes_on_path_to_root:
                return iter0
            nodes_on_path_to_root.add(iter0)
            iter0 = iter0.parent
        if iter1:
            if iter1 in nodes_on_path_to_root:
                return iter1
            nodes_on_path_to_root.add(iter1)
            iter1 = iter1.parent

    raise ValueError('node0 and node1 are not in the same tree')
