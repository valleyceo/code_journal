# LC 1579. Remove Max Number of Edges to Keep Graph Fully Traversable

'''
Alice and Bob have an undirected graph of n nodes and three types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can be traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional edge of type typei between nodes ui and vi, find the maximum number of edges you can remove so that after removing the edges, the graph can still be fully traversed by both Alice and Bob. The graph is fully traversed by Alice and Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if Alice and Bob cannot fully traverse the graph.
'''

# O(E + V) time | O(V) space
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(x, root):
            if x != root[x]:
                root[x] = find(root[x], root)

            return root[x]

        def union(x, y, root):
            root_x = find(x, root)
            root_y = find(y, root)

            if root_x != root_y:
                root[root_y] = root_x
                return True

            return False

        res = 0
        a_ct = 0
        b_ct = 0
        ab_root = [i for i in range(n + 1)]

        for t, i, j in edges:
            if t == 3:
                if union(i, j, ab_root):
                    a_ct += 1
                    b_ct += 1
                else:
                    res += 1

        a_root = ab_root[:]
        b_root = ab_root[:]

        for t, i, j in edges:
            if t == 1:
                if union(i, j, a_root):
                    a_ct += 1
                else:
                    res += 1
            elif t == 2:
                if union(i, j, b_root):
                    b_ct += 1
                else:
                    res += 1

        return res if a_ct == b_ct == n - 1 else -1
