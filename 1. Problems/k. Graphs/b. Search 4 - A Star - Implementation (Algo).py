# A* Algorithm

'''
Given a matrix of 0 (passable) and 1 (block), and a starting and ending coordinate, return path
'''
import heapq

class Node:
	def __init__(self, row, col, value):
		self.id = str(row) + "-" + str(col)
		self.row = row
		self.col = col
		self.val = value
		self.pDist = float("inf")
		self.eDist = float("inf")
		self.prev = None
		
	def __lt__(self, other):
		return self.eDist < other.eDist
		
def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    M = initNodes(graph)
	endPoint = [endRow, endCol]
	M[startRow][startCol].pDist = 0
	M[startRow][startCol].eDist = 0
	que = [M[startRow][startCol]]
	
	while que:
		node = heapq.heappop(que)
		
		if [node.row, node.col] == endPoint:
			break
		
		neighbors = getNeighbors(node.row, node.col, M)
		d = M[node.row][node.col].pDist + 1
		
		for r2, c2 in neighbors:
			
			if d >= M[r2][c2].pDist:
				continue
			
			M[r2][c2].prev = node
			M[r2][c2].pDist = d
			M[r2][c2].eDist = d + getDist([r2, c2], endPoint)
			
			heapq.heappush(que, M[r2][c2])
			
	return reconstructPath(M[endRow][endCol])

def reconstructPath(node):
	if not node.prev:
		return []
	
	curr = node
	path = []
	
	while curr:
		path.append([curr.row, curr.col])
		curr = curr.prev
		
	return path[::-1]
	
def getNeighbors(i, j, M):
	neighbors = []
	
	for dr, dc in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
		r = i + dr
		c = j + dc
		
		if r < 0 or r >= len(M) or c < 0 or c >= len(M[0]) or M[r][c].val == 1:
			continue
			
		neighbors.append([r, c])
	
	return neighbors

def initNodes(M):
	R = len(M)
	C = len(M[0])
	return [[Node(r, c, M[r][c]) for c in range(C)] for r in range(R)]
	
def getDist(p1, p2):
	return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])