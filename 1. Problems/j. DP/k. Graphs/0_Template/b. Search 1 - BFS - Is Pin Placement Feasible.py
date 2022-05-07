# Is Pin Placement Feasible

'''
- Given a set of pins and wires connecting pairs of pins (either left or right)
- Determine if it is possible to place the pins such that their immediate neighbor is always the opposite
- Return such division if one exists

* Other term for this problem: bipartite graphs, 2-colorable
'''
# Time complexity: O(p + w), p: path, w: number of wires, BFS
# Space complexity: O(p)
class GraphVertex:
    def __init__(self) -> None:
        self.d = -1
        self.edges: List[GraphVertex] = []


def is_any_placement_feasible(graph: List[GraphVertex]) -> bool:
    def bfs(s):
        s.d = 0
        q = collections.deque([s])

        while q:
            for t in q[0].edges:
                if t.d == -1:  # Unvisited vertex.
                    t.d = q[0].d + 1
                    q.append(t)
                elif t.d == q[0].d:
                    return False
            del q[0]
        return True

    return all(bfs(v) for v in graph if v.d == -1)
