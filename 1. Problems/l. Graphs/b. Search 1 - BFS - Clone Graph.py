# LC 133. Clone Graph

'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
'''
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.iterative(node)

    # O(N + M) time | O(N) space
    # N is number of nodes and M is number of edges
    def recursive(self, node: 'Node', visited: set) -> 'Node':
        if not node:
            return node

        if node in visited:
            return visited[node]

        cloneNode = Node(node.val, [])
        visited[node] = cloneNode

        if node.neighbors:
            for n in node.neighbors:
                cloneNode.neighbors.append(self.dfs(n, visited))

        return cloneNode

    # O(N + M) time | O(N) space
    def iterative(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}
        copy_node = Node(node.val)
        queue = deque([node])
        visited[node] = copy_node

        while queue:
            next_node = queue.popleft()

            for child_node in next_node.neighbors:
                if child_node not in visited:
                    copy_node = Node(child_node.val)
                    visited[child_node] = copy_node
                    queue.append(child_node)

                visited[next_node].neighbors.append(visited[child_node])

        return visited[node]
