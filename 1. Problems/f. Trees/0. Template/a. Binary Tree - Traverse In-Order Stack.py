class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inOrder(root):

    current = root
    stack = []

    while True:
        if current is not None:
            stack.append(current)
            current = current.left

        elif(stack):
            current = stack.pop()
            print(current.data, end=" ")
            current = current.right

        else:
            break

def inorder_traversal(tree: BinaryTreeNode) -> List[int]:

    result = []

    in_process = [(tree, False)]
    while in_process:
        node, left_subtree_traversed = in_process.pop()
        if node:
            if left_subtree_traversed:
                result.append(node.data)
            else:
                in_process.append((node.right, False))
                in_process.append((node, True))
                in_process.append((node.left, False))
    return result
