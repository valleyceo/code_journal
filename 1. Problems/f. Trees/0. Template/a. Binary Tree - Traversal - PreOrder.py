# Implement Pre-order Traversal without Recursion

# O(n) time | O(h) space
def preorder_traversal(tree: BinaryTreeNode) -> List[int]:

    result = []

    in_process = [(tree, False)]
    while in_process:
        node, node_processed = in_process.pop()
        if node:
            if node_processed:
                result.append(node.data)
            else:
                in_process.append((node.right, False))
                in_process.append((node.left, False))
                in_process.append((node, True))
    return result
