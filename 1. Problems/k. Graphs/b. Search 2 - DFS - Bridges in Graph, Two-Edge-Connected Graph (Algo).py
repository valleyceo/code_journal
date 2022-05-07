# Two-Edge-Connected Graph

'''
Given a list of Edges, return True if graph is two-edge-connected
'''
# Bridges in Graph problem, O(V + E) time | O(V) space
def twoEdgeConnectedGraph(edges):
	if len(edges) == 0:
		return True
	
	arrivalTimes = [-1] * len(edges)
	start = 0
	
	if dfs(start, -1, 0, arrivalTimes, edges) == -1:
		return False
	
	return areAllVisited(arrivalTimes)

def dfs(curr, parent, time, arrivalTimes, edges):
	arrivalTimes[curr] = time
	minTime = time
	
	for node in edges[curr]:
		if arrivalTimes[node] == -1:
			minTime = min(minTime, dfs(node, curr, time + 1, arrivalTimes, edges))
		elif node != parent and minTime > arrivalTimes[node]:
			minTime = min(minTime, arrivalTimes[node])
	
	if minTime == time and parent != -1:
		return -1
	
	return minTime

def areAllVisited(arrivalTimes):
	for t in arrivalTimes:
		if t == -1:
			return False
		
	return True