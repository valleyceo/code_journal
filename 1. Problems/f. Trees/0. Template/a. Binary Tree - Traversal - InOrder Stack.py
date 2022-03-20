class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        res = []
        curr = root

        while len(stack) > 0 or curr is not None:
            while curr is not None:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res


'''
Other Versions
'''
def inorderTraversal(self, root: TreeNode) -> List[int]:
    stack = []
    res = []
    curr = root

    while True:

        if curr:
            stack.append(curr)
            curr = curr.left
        elif len(stack) > 0:
            curr = stack.pop()
            res += [curr.val]

            curr = curr.right
        else:
            break

    return res

def inorderTraversal(tree: BinaryTreeNode) -> List[int]:

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
