# Airport Connections

'''
Given list of airports and list of airports flights, return minimum number of extra flights needed such that all flights are connected from starting airport
'''
# O(a * (a + r) + a + r + alog(a)) time | O(a + r) space
def airportConnections(airports, routes, startingAirport):
    graph = createGraph(airports, routes) # Create graph with nodes of each airport
	reachableNodes = getReachableNodes(graph, airports, startingAirport) # Fill isReachable for each node
	markReachableConnections(graph, reachableNodes) # Fill unreachable list for each unreachable airports
	
	return getMinNumberOfNewConnections(graph, reachableNodes) # Starting with the least

def getMinNumberOfNewConnections(graph, reachables):
	reachables.sort(key = lambda node : len(node.reachables), reverse = True)
	countConnections = 0
	
	for node in reachables:
		if node.isReachable:
			continue
		
		countConnections += 1
		
		for node in node.reachables:
			graph[node].isReachable = True
	
	return countConnections

def markReachableConnections(graph, reachables):
	
	for node in reachables:
		name = node.name
		reachables = []
		findReachablesDFS(graph, name, reachables, {})
		node.reachables = reachables

def findReachablesDFS(graph, node, reachables, visited):
	if graph[node].isReachable:
		return
	
	if node in visited:
		return
	
	visited[node] = True
	reachables.append(node)
	
	for nextNode in graph[node].neighbors:
		findReachablesDFS(graph, nextNode, reachables, visited)
	
def getReachableNodes(graph, nodeList, start):
	visited = {}
	dfs(graph, start, visited)
	
	reachable = []
	
	for node in nodeList:
		if node in visited:
			continue
		
		curr = graph[node]
		curr.isReachable = False
		reachable.append(curr)
	
	return reachable

def dfs(graph, node, visited):
	if node in visited:
		return
	
	visited[node] = True
	
	for nextNode in graph[node].neighbors:
		dfs(graph, nextNode, visited)
	
def createGraph(nodeList, edges):
	graph = {}
	
	for node in nodeList:
		graph[node] = Node(node)
		
	for e in edges:
		graph[e[0]].neighbors.append(e[1])
		
	return graph

class Node:
	def __init__(self, name):
		self.name = name
		self.neighbors = []
		self.isReachable = True
		self.reachables = []