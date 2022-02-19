# Generate Binary Tree (need to review)

'''
- Given a number
- Return all distinct binary trees with that numbers
'''

# O((2n)!/(n!(n+1)!)) time
def generate_all_binary_trees(num_nodes: int
                              ) -> List[Optional[BinaryTreeNode]]:

    if num_nodes == 0:  # Empty tree, add as a None.
        return [None]

    result: List[Optional[BinaryTreeNode]] = []
    for num_left_tree_nodes in range(num_nodes):
        num_right_tree_nodes = num_nodes - 1 - num_left_tree_nodes
        left_subtrees = generate_all_binary_trees(num_left_tree_nodes)
        right_subtrees = generate_all_binary_trees(num_right_tree_nodes)
        # Generates all combinations of left_subtrees and right_subtrees.
        result += [
            BinaryTreeNode(0, left, right) for left in left_subtrees
            for right in right_subtrees
        ]
    return result


def generate_all_binary_trees_pythonic(num_nodes):
    return [
        BinaryTreeNode(0, left, right)
        for num_left_tree_nodes in range(num_nodes)
        for left in generate_all_binary_trees(num_left_tree_nodes)
        for right in generate_all_binary_trees(num_nodes - 1 -
                                               num_left_tree_nodes)
    ] or [None]


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result
