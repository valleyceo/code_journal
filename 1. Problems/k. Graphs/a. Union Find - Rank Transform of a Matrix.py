# LC 1632. Rank Transform of a Matrix

'''
Given an m x n matrix, return a new matrix answer where answer[row][col] is the rank of matrix[row][col].

The rank is an integer that represents how large an element is compared to other elements. It is calculated using the following rules:

The rank is an integer starting from 1.
If two elements p and q are in the same row or column, then:
If p < q then rank(p) < rank(q)
If p == q then rank(p) == rank(q)
If p > q then rank(p) > rank(q)
The rank should be as small as possible.
The test cases are generated so that answer is unique under the given rules.
'''

class UnionFind:
    def __init__(self, graph):
        self.p = {i:i for i in graph}

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)

    def groups(self):
        ans = defaultdict(list)
        for el in self.p.keys():
            ans[self.find(el)].append(el)
        return ans

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        d = defaultdict(list)

        for i, j in product(range(n), range(m)):
            d[matrix[i][j]].append([i, j])

        for a in sorted(d):
            graph = [i for i, j in d[a]] + [j + n for i, j in d[a]]
            uf = UnionFind(graph)

            for i, j in d[a]:
                uf.union(i, j + n)

            for group in uf.groups().values():
                mx = max(rank[i] for i in group)
                for i in group:
                    rank[i] = mx + 1

            for i, j in d[a]:
                matrix[i][j] = rank[i]

        return matrix
