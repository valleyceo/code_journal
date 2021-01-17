"""
Dijkstra:
- BFS search that respects edge cost
  
Usage:
- Find the minimal path sum from starting node to each other node
"""

import heapq

def dijkstra(graph, start_node):
    nodePathSum = {vertex: float('infinity') for vertex in graph}
    nodePathSum[start_node] = 0

    pque = [(0, start_node)]

    while pque:
        current_dist, current_node = heapq.heappop(pque)

        if current_dist > nodePathSum[current_node]:
            continue  # already found a better path

        for neighbor, weight in graph[current_node].items():
            d = current_dist + weight

            if d < nodePathSum[neighbor]:
                nodePathSum[neighbor] = d
                heapq.heappush(pque, (d, neighbor))

    return nodePathSum