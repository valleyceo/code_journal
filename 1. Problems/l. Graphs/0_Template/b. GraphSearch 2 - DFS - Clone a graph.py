class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfs(node, {})
        
    def dfs(self, node: 'Node', visited: set) -> 'Node':
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