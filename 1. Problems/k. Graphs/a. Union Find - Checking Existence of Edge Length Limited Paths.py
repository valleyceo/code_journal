# LC 1697. Checking Existence of Edge Length Limited Paths

'''
An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.
'''

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx != ry:
            self.root[ry] = rx

# O(QlogQ + NlogN) time | O(N) space
class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:

        queriesSorted = sorted([limit, n1, n2, i] for i, (n1, n2, limit) in enumerate(queries))
        edgeListSorted = sorted([(w, e1, e2) for e1, e2, w in edgeList])
        uf = UnionFind(n)
        idx = 0
        res = [0] * len(queries)

        for l, n1, n2, i in queriesSorted:
            while idx < len(edgeListSorted) and edgeListSorted[idx][0] < l:
                _, e1, e2 = edgeListSorted[idx]
                uf.union(e1, e2)
                idx += 1

            res[i] = uf.find(n1) == uf.find(n2)

        return res
