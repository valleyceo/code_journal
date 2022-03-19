# LC 2203. Minimum Weighted Subgraph With the Required Paths

'''
You are given an integer n denoting the number of nodes of a weighted directed graph. The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The weight of a subgraph is the sum of weights of its constituent edges.
'''
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:

        def dijkstra(src, graph):
            pArr = [(0, src)]
            dist_map = {}

            while pArr:
                dist, node = heapq.heappop(pArr)

                if node in dist_map:
                    continue

                dist_map[node] = dist

                for next_node, next_dist in graph[node]:
                    heapq.heappush(pArr, (dist + next_dist, next_node))

            return [dist_map.get(i, float('inf')) for i in range(n)]

        G1 = defaultdict(list)
        G2 = defaultdict(list)

        for s, d, w in edges:
            G1[s].append([d, w])
            G2[d].append([s, w])

        arr1 = dijkstra(src1, G1)
        arr2 = dijkstra(src2, G1)
        arr3 = dijkstra(dest, G2)

        res = float('inf')

        for i in range(n):
            res = min(res, arr1[i] + arr2[i] + arr3[i])

        return res if res != float('inf') else -1
