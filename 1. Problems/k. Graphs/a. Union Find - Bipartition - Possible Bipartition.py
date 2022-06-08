# LC 886. Possible Bipartition

'''
We want to split a group of n people (labeled from 1 to n) into two groups of any size. Each person may dislike some other people, and they should not go into the same group.

Given the integer n and the array dislikes where dislikes[i] = [ai, bi] indicates that the person labeled ai does not like the person labeled bi, return true if it is possible to split everyone into two groups in this way.
'''

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])

        return self.root[x]

    def union(self, x, y, py):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            self.root[root_y] = root_x

        return root_x == py


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        return self.unionFind(n, dislikes)

    def unionFind(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for n1, n2 in dislikes:
            graph[n1 - 1].append(n2 - 1)
            graph[n2 - 1].append(n1 - 1)

        uf = UnionFind(n)

        for n1 in range(n):
            p1 = uf.find(n1)

            if p1 in graph:
                dl1 = uf.find(graph[n1][0])

                for dl2 in graph[n1][1:]:
                    if uf.union(dl2, dl1, p1): # Combine all dislikes, if any root equals parent of node1, then return False
                        return False

        return True

    def colorCode(self, n: int, dislikes: List[List[int]]) -> bool:

        def helper(i, color):
            colors[i] = color

            for j in dislike_graph[i]:
                if colors[j] == color:
                    return False

                if colors[j] == 0 and not helper(j, -color):
                    return False

            return True

        dislike_graph = defaultdict(list)
        colors = defaultdict(int)

        for n1, n2 in dislikes:
            dislike_graph[n1 - 1].append(n2 - 1)
            dislike_graph[n2 - 1].append(n1 - 1)

        for i in range(n):
            if colors[i] == 0 and not helper(i, 1):
                return False

        return True
