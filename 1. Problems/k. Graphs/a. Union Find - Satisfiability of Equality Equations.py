# LC 990. Satisfiability of Equality Equations

'''
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
'''

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if x == self.root[x]:
            return x

        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.root[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.root[rootX] = rootY
            else:
                self.root[rootY] = rootX
                self.rank[rootX] += 1

    def connected(self, x, y):
        return self.find(x) == self.find(y)

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        return self.colorCodeDFS(equations)

    # O(N) time | O(1) space
    def unionFind(self, equations: List[str]) -> bool:
        uf = UnionFind(26)
        oa = ord('a')

        for eqn in equations:
            if eqn[1] == "=":
                uf.union(ord(eqn[0]) - oa, ord(eqn[3]) - oa)

        for eqn in equations:
            if eqn[1] == "!" and uf.connected(ord(eqn[0]) - oa, ord(eqn[3]) - oa):
                return False

        return True

    # O(N) time | O(1) space
    def colorCodeDFS(self, equations: List[str]) -> bool:

        def dfs(start, color, color_map, graph):
            queue = [start]
            color_map[start] = color

            while queue:
                node = queue.pop()

                for next_node in graph[node]:
                    if color_map[next_node] == None:
                        color_map[next_node] = color
                        queue.append(next_node)

        graph = [[] for _ in range(26)]
        oa = ord('a')

        for eqn in equations:
            if eqn[1] == "=":
                l = ord(eqn[0]) - oa
                r = ord(eqn[3]) - oa

                graph[l].append(r)
                graph[r].append(l)

        color_map = [None] * 26
        color = 1

        for node in range(26):
            if color_map[node] is None:
                dfs(node, color, color_map, graph)
                color += 1

        for eqn in equations:
            if eqn[1] == "!":
                l = ord(eqn[0]) - oa
                r = ord(eqn[3]) - oa

                if l == r:
                    return False

                if color_map[l] is not None and color_map[l] == color_map[r]:
                    return False

        return True
