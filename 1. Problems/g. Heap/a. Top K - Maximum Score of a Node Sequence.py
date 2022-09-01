# LC 2242. Maximum Score of a Node Sequence

'''
There is an undirected graph with n nodes, numbered from 0 to n - 1.

You are given a 0-indexed integer array scores of length n where scores[i] denotes the score of node i. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A node sequence is valid if it meets the following conditions:

There is an edge connecting every pair of adjacent nodes in the sequence.
No node appears more than once in the sequence.
The score of a node sequence is defined as the sum of the scores of the nodes in the sequence.

Return the maximum score of a valid node sequence with a length of 4. If no such sequence exists, return -1.
'''

# O(E + V) time | O(E + V) space
class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        res = -1
        graph = defaultdict(list)

        for e1, e2 in edges:
            heapq.heappush(graph[e1], [scores[e2], e2])
            heapq.heappush(graph[e2], [scores[e1], e1])

            if len(graph[e1]) > 3:
                heapq.heappop(graph[e1])

            if len(graph[e2]) > 3:
                heapq.heappop(graph[e2])

        for e1, e2 in edges:
            for v11, e11 in graph[e1]:
                for v22, e22 in graph[e2]:
                    if e11 != e22 and e11 != e2 and e22 != e1:
                        res = max(res, v11 + v22 + scores[e1] + scores[e2])

        return res
