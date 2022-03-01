# 427. Construct Quad Tree

'''
Given a n * n matrix grid of 0's and 1's only. We want to represent the grid with a Quad-Tree.

Return the root of the Quad-Tree representing the grid.

Notice that you can assign the value of a node to True or False when isLeaf is False, and both are accepted in the answer.

A Quad-Tree is a tree data structure in which each internal node has exactly four children. Besides, each node has two attributes:

val: True if the node represents a grid of 1's or False if the node represents a grid of 0's.
isLeaf: True if the node is leaf node on the tree or False if the node has the four children.

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
'''
#O(N*log2(N)*log2(N)) time (not sure) | O(N^2) space
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n = len(grid)
        mid = n // 2

        if self.isLeaf(grid):
            return Node(grid[0][0], True, None, None, None)

        node = Node(1, False, None, None, None, None)
        node.topLeft = self.construct(self.sliceMatrix(grid, 0, 0, mid))
        node.topRight = self.construct(self.sliceMatrix(grid, 0, mid, mid))
        node.bottomLeft = self.construct(self.sliceMatrix(grid, mid, 0, mid))
        node.bottomRight = self.construct(self.sliceMatrix(grid, mid, mid, mid))

        return node

    def isLeaf(self, grid: List[List[int]]) -> bool:

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != grid[0][0]:
                    return False

        return True

    def sliceMatrix(self, grid: List[List[int]], ridx, cidx, n) -> List[List[int]]:
        subgrid = []

        for i in range(ridx, ridx + n):
            temp = []
            for j in range(cidx, cidx + n):
                temp.append(grid[i][j])

            subgrid.append(temp)

        return subgrid
