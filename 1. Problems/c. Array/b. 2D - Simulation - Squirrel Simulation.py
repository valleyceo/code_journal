# LC 573. Squirrel Simulation

'''
You are given two integers height and width representing a garden of size height x width. You are also given:

an array tree where tree = [treer, treec] is the position of the tree in the garden,
an array squirrel where squirrel = [squirrelr, squirrelc] is the position of the squirrel in the garden,
and an array nuts where nuts[i] = [nutir, nutic] is the position of the ith nut in the garden.
The squirrel can only take at most one nut at one time and can move in four directions: up, down, left, and right, to the adjacent cell.

Return the minimal distance for the squirrel to collect all the nuts and put them under the tree one by one.

The distance is the number of moves.
'''
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        def getDist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        res = 0
        max_start_dist = float("-inf")

        for nut in nuts:
            res += getDist(nut, tree) * 2
            max_start_dist = max(max_start_dist, getDist(nut, tree) - getDist(nut, squirrel))

        return res - max_start_dist

"""
Insight:
    - Only 1 nut will have passage from squirrel and tree, the rest nuts will simply be nuts to tree times two.
    - For the 1 nut, you want to pick the furthest nut from the tree but closer one with the squirrel to minimize cost
        - Imagine one nut between tree and squirrel, one nut further away, and one opposite side of tree. The further away (not opposite to tree) saves the most distance.
"""
