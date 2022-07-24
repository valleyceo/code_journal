# LC 2277. Closest Node to Path in Tree

'''
You are given a positive integer n representing the number of nodes in a tree, numbered from 0 to n - 1 (inclusive). You are also given a 2D integer array edges of length n - 1, where edges[i] = [node1i, node2i] denotes that there is a bidirectional edge connecting node1i and node2i in the tree.

You are given a 0-indexed integer array query of length m where query[i] = [starti, endi, nodei] means that for the ith query, you are tasked with finding the node on the path from starti to endi that is closest to nodei.

Return an integer array answer of length m, where answer[i] is the answer to the ith query.
'''

class Solution:
    def closestNode(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        def getPathBFS(s_node, e_node, G):
            seen = set([s_node])
            queue = [[1, s_node, seen]]

            while queue:
                count, node, seen = heapq.heappop(queue)

                if node == e_node:
                    return seen

                for next_node in G[node]:
                    if next_node in seen:
                        continue

                    seen2 = seen.copy()
                    seen2.add(next_node)
                    heapq.heappush(queue, [count + 1, next_node, seen2])

        def searchClosestNodeInPathBFS(f_node, path, G):

            queue = [[i] for i in path]
            visited = path.copy()
            dist = 0

            while queue:
                temp = []

                for node_path in queue:
                    node = node_path[-1]

                    if node == f_node:
                        return node_path[0]

                    for next_node in G[node]:
                        if next_node in visited:
                            continue

                        visited.add(next_node)
                        temp.append(node_path + [next_node])

                queue = temp

        res = []

        for s, e, n in query:
            path_set = getPathBFS(s, e, graph)
            res.append(searchClosestNodeInPathBFS(n, path_set, graph))

        return res
