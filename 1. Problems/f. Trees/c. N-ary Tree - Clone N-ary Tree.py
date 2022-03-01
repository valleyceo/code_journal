# LC 1490. Clone N-ary Tree

'''
Given a root of an N-ary tree, return a deep copy (clone) of the tree.

Each node in the n-ary tree contains a val (int) and a list (List[Node]) of its children.

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).

Example 1:

Input: root = [1,null,3,2,4,null,5,6]
Output: [1,null,3,2,4,null,5,6]

Example 2:

Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
Output: [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]

Constraints:
The depth of the n-ary tree is less than or equal to 1000.
The total number of nodes is between [0, 104].
'''
# O(n) time | O(n) space
class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        return self.recursive(root)

    def recursive(self, root: 'Node') -> 'Node':
        if root is None:
            return

        node = Node(root.val)

        for child in root.children:
            node.children.append(self.cloneTree(child))

        return node

    def iterative(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        node = Node(root.val)
        stack = [(root, node)]

        while stack:
            old_node, copy_node = stack.pop()

            for child_node in old_node.children:
                node = Node(child_node.val)
                copy_node.children.append(node)
                stack.append((child_node, node))

        return node
