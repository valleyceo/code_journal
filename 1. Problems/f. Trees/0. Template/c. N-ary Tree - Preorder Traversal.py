class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

# N-ary Tree Preorder Traversal
# O(n) time | O(n) space
class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if root is None:
            return []

        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])

        return output
