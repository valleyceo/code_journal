# 2316. Count Unreachable Pairs of Nodes in an Undirected Graph

'''
You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.
'''
# O(n + edges) time | O(n) space
class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root != y_root:
            if self.rank[x_root] > self.rank[y_root]:
                self.parent[y_root] = x_root

            elif self.rank[x_root] < self.rank[y_root]:
                self.parent[x_root] = y_root
            else:
                self.parent[y_root] = x_root
                self.rank[x_root] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)
        res = 0

        for x, y in edges:
            uf.union(x, y)

        counter = defaultdict(int)

        for i in range(n):
            i_root = uf.find(i)
            counter[i_root] += 1

        if len(counter) == 0:
            return 0

        for k, v in counter.items():
            res += v * (n - v)

        return res // 2
