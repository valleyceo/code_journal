# Clone a Graph (need to review)

'''
- Given a directed graph and a reference vertex u
- Create a copy of graph that is reachable from u
'''
# Time complexity: O(|V|+|E|) | Space complexity: O(|V|)
class GraphVertex:
    def __init__(self, label: int) -> None:
        self.label = label
        self.edges: List['GraphVertex'] = []


def clone_graph(graph: GraphVertex) -> GraphVertex:

    if graph is None:
        return None

    q = collections.deque([graph])
    vertex_map = {graph: GraphVertex(graph.label)}
    while q:
        v = q.popleft()
        for e in v.edges:
            # Try to copy vertex e.
            if e not in vertex_map:
                vertex_map[e] = GraphVertex(e.label)
                q.append(e)
            # Copy edge.
            vertex_map[v].edges.append(vertex_map[e])
    return vertex_map[graph]
