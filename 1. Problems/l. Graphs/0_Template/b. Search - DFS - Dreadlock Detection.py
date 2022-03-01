# Deadlock Detection (need to review)

'''
- Given a directed graph
- Check if the graph contains a cycle (has a deadlock)

- Deadlock: A situation in which two or more competing actions are each waiting for the other to finish
- Circular graph is sufficient for deadlock but not necessary (depends on OS)
- Node markings: white (never discovered), gray (first discovered), black (finished processing)
'''
class GraphVertex:

    WHITE, GRAY, BLACK = range(3)

    def __init__(self) -> None:

        self.color = GraphVertex.WHITE

        self.edges: List['GraphVertex'] = []

# O(|V| + |E|) time
def is_deadlocked(graph: List[GraphVertex]) -> bool:
    def has_cycle(cur):
        # Visiting a gray vertex means a cycle.
        if cur.color == GraphVertex.GRAY:
            return True

        cur.color = GraphVertex.GRAY  # Marks current vertex as a gray one.
        # Traverse the neighbor vertices.
        if any(next.color != GraphVertex.BLACK and has_cycle(next)
               for next in cur.edges):
            return True
        cur.color = GraphVertex.BLACK  # Marks current vertex as black.
        return False

    return any(vertex.color == GraphVertex.WHITE and has_cycle(vertex)
               for vertex in graph)
