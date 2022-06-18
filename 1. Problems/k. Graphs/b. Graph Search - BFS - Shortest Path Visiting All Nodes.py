# LC 847. Shortest Path Visiting All Nodes

'''
You have an undirected, connected graph of n nodes labeled from 0 to n - 1. You are given an array graph where graph[i] is a list of all the nodes connected with node i by an edge.

Return the length of the shortest path that visits every node. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.
'''
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        return self.bfsSolution(graph)

    # O(2^N * N^2) time | O(2^N * N^2) space
    def dfsSolution(self, graph: List[List[int]]) -> int:

        def dfs(node, mask):
            key = (node, mask)

            if key in cache:
                return cache[key]

            if mask & (mask - 1) == 0:
                return 0

            cache[key] = float('inf')

            for next_node in graph[node]:
                if mask & (1 << next_node) == 0:
                    continue

                skip = 1 + dfs(next_node, mask)
                use = 1 + dfs(next_node, mask ^ (1 << node))
                cache[key] = min(cache[key], use, skip)

            return cache[key]

        cache = {}
        n = len(graph)
        mask = (1 << n) - 1

        return min(dfs(i, mask) for i in range(n))

    # O(2^N * N^2) time | O(2^N * N^2) space
    def bfsSolution(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return 0

        n = len(graph)
        full_mask = (1 << n) - 1
        queue = [(i, 1 << i) for i in range(n)]
        visited = set(queue)
        step = 0

        while queue:
            next_queue = []

            for i in range(len(queue)):
                node, mask = queue[i]

                for next_node in graph[node]:
                    next_mask = mask | (1 << next_node)

                    if next_mask == full_mask:
                        return 1 + step

                    if (next_node, next_mask) in visited:
                        continue

                    visited.add((next_node, next_mask))
                    next_queue.append((next_node, next_mask))

            step += 1
            queue = next_queue

        return -1
