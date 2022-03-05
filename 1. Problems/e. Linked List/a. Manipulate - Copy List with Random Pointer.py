# LC 138. Copy List with Random Pointer

'''
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
'''
class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        return self.interleavingSolution(head)

    # O(n) time | O(1) space
    def interleavingSolution(self, head: 'Node') -> 'Node':
        if not head:
            return head

        ptr = head
        ptr = head
        while ptr:
            # Interleave  A->B->C to A->A'->B->B'->C->C'
            ptr.next = Node(ptr.val, ptr.next)
            ptr = ptr.next.next

        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None
            ptr = ptr.next.next

        ptr_old = head
        ptr_new = head.next
        head_new = head.next
        while ptr_old:
            ptr_old.next = ptr_old.next.next
            ptr_new.next = ptr_new.next.next if ptr_new.next else None

            ptr_old = ptr_old.next
            ptr_new = ptr_new.next

        return head_new

    # O(n) time | O(n) space
    def iterativeSolution(self, root: 'Node') -> 'Node':
        def getClonedNode(n):
            if not n:
                return

            if n in self.visited:
                return self.visited[n]
            else:
                self.visited[n] = Node(n.val)
                return self.visited[n]

        if root == None:
            return None

        curr_node = root
        copy_node = Node(curr_node.val)
        self.visited[curr_node] = copy_node

        while curr_node:
            copy_node.next = getClonedNode(curr_node.next)
            copy_node.random = getClonedNode(curr_node.random)

            curr_node = curr_node.next
            copy_node = copy_node.next

        return self.visited[root]

    # O(n) time | O(n) space
    def recursiveSolution(self, node: 'Node') -> 'Node':
        if node == None:
            return None

        if node in self.visited:
            return self.visited[node]

        copy_node = Node(node.val)
        self.visited[node] = copy_node

        copy_node.next = self.recursiveSolution(node.next)
        copy_node.random = self.recursiveSolution(node.random)

        return copy_node
