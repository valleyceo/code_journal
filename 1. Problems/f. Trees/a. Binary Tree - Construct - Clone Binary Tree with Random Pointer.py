# LC 1485. Clone Binary Tree With Random Pointer

'''
A binary tree is given such that each node contains an additional random pointer which could point to any node in the tree or null.

Return a deep copy of the tree.

The tree is represented in the same input/output way as normal binary trees where each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (in the input) where the random pointer points to, or null if it does not point to any node.
You will be given the tree in class Node and you should return the cloned tree in class NodeCopy. NodeCopy class is just a clone of Node class with the same attributes and constructors.

Constraints:
The number of nodes in the tree is in the range [0, 1000].
1 <= Node.val <= 10^6

# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random
'''
class Solution:
    def copyRandomBinaryTree(self, root: 'Optional[Node]') -> 'Optional[NodeCopy]':
        return self.copyTree(root, {})

    def copyTree(self, node: 'Optional[Node]', treemap: dict) -> 'Optional[NodeCopy]':
        if node is None:
            return node

        if node in treemap:
            return treemap[node]

        copy_node = NodeCopy(node.val)
        treemap[node] = copy_node
        copy_node.left = self.copyTree(node.left, treemap)
        copy_node.right = self.copyTree(node.right, treemap)
        copy_node.random = self.copyTree(node.random, treemap)

        return copy_node
