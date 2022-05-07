# Team Photo Day 2 (need to review)

'''
- Given the same team photo problem
- Determine the largest number of teams that can be photographed simultaneously
'''
# O(|V| + |E|) time
class GraphVertex:
    def __init__(self) -> None:
        self.edges: List[GraphVertex] = []
        # Set max_distance = 0 to indicate unvisitied vertex.
        self.max_distance = 0


def find_largest_number_teams(graph: List[GraphVertex]) -> int:
    def dfs(curr):
        curr.max_distance = max(
            ((vertex.max_distance if vertex.max_distance != 0 else dfs(vertex))
             + 1 for vertex in curr.edges),
            default=1)
        return curr.max_distance

    return max(dfs(g) for g in graph if g.max_distance == 0)
