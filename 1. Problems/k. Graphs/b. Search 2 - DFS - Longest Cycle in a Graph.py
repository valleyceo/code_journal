# LC 2360. Longest Cycle in a Graph

'''
You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.
'''

class Solution:
    def longestCycle(self, edges: List[int]) -> int:

        res = -1
        
        def dfs(node):
            dist = 0
            dist_map = {}
            curr = node

            while curr != -1:

                if curr in dist_map:
                    return dist - dist_map[curr]

                dist_map[curr] = dist
                x = edges[curr]
                edges[curr] = -1
                curr = x
                dist += 1

            return -1

        for i in range(len(edges)):
            if edges[i] == -1:
                continue

            res = max(res, dfs(i))

        return res
