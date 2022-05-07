def dijkstrasAlgorithm(start, edges):
    n_vertices = len(edges)

	minDist = [float('inf') for _ in range(n_vertices)]
	minDist[start] = 0
	visited = set()

	while len(visited) != n_vertices:
		vertex, currDist = getVertexWithMinDist(minDist, visited)

		if currDist == float('inf'):
			break

		visited.add(vertex)

		for edge in edges[vertex]:

			if edge[0] in visited:
				continue

			nextDist = currDist + edge[1]

			if nextDist < minDist[edge[0]]:
				minDist[edge[0]] = nextDist

	return list(map(lambda x: -1 if x == float('inf') else x, minDist))

def getVertexWithMinDist(distances, visited):
	currentMinDist = float('inf')
	minVertex = -1

	for vIdx, dist in enumerate(distances):
		if vIdx in visited:
			continue

		if dist <= currentMinDist:
			minVertex = vIdx
			currentMinDist = dist

	return minVertex, currentMinDist
