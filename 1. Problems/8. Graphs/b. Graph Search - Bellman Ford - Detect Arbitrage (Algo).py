# Detect Arbitrage

'''
Given a matrix of exchange rate, see if there is an arbitrage. Arbitrage happens when you exchange rates and end up gaining more than your original amount.
'''

import math

# Bellman Ford O(n^3) time | O(n^2) space
def detectArbitrage(exchangeRates):
	logRates = convertLog(exchangeRates)
	
	return bellmanFord(logRates, 0)

def bellmanFord(graph, start):
	dist = [float("inf") for _ in range(len(graph))]
	dist[start] = 0
	
	for _ in range(len(graph) - 1):
		if not updateDist(graph, dist):
			return False
	
	return updateDist(graph, dist)

def updateDist(graph, dist):
	updated = False
	
	for i in range(len(graph)):
		for j in range(len(graph)):
			if i == j:
				continue
			
			newDist = dist[i] + graph[i][j]
			
			if newDist < dist[j]:
				updated = True
				dist[j] = newDist
	
	return updated
 
def convertLog(M):
	return [[-math.log10(M[i][j]) for i in range(len(M))] for j in range(len(M[0]))]


'''
Brute force solution
'''
from collections import defaultdict

# O(n^n) time | O(n^3) space
def detectArbitrage(exchangeRates):
    graph = buildGraph(exchangeRates)
	
	for i in range(len(exchangeRates)):
		if isProfitable(i, graph):
			return True
		
	return False
	
def buildGraph(matrix):
	if len(matrix) == 0:
		return {}
	
	graph = defaultdict(dict)
	
	for i in range(len(matrix)):
		for j in range(len(matrix)):
			if i == j:
				continue
			
			graph[i][j] = matrix[i][j]
	
	return graph

def isProfitable(node, graph):
	que = []
	
	for i in range(len(graph)):
		if i == node:
			continue
		
		visited = set([node, i])
		que.append([i, graph[node][i], visited])
	
	while que:
		currNode, currVal, currSet = que.pop()
		
		for i in range(len(graph)):
			if i == node and currVal * graph[currNode][i] > 1:
				return True
			
			if i not in currSet:
				newSet = currSet.copy()
				newSet.add(i)
				que.append([i, currVal * graph[currNode][i], newSet])
	
	return False