# LC 116. Populating Next Right Pointers in Each Node

'''
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Constraints:
The number of nodes in the tree is in the range [0, 212 - 1].
-1000 <= Node.val <= 1000

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        return self.bfsOptimal(root)

    # assumes perfect binary tree
    def bfsOptimal(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        leftmost = root

        while leftmost.left:
            head = leftmost

            while head:
                head.left.next = head.right

                if head.next:
                    head.right.next = head.next.left

                head = head.next

            leftmost = leftmost.left

        return root

    # works on any binary tree
    def bfs(self, root: 'Node') -> 'Node':
        if root is None:
            return root

        level = [root]

        while level:
            temp = []

            for i in range(len(level)):
                if i == 0:
                    temp_node = level[i]
                else:
                    temp_node.next = level[i]
                    temp_node = level[i]

                if level[i].left:
                    temp.append(level[i].left)

                if level[i].right:
                    temp.append(level[i].right)

            level = temp

        return root
