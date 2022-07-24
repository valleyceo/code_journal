# LC 2337. Move Pieces to Obtain a String

'''
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target by moving the pieces of the string start any number of times. Otherwise, return false.

Input: start = "_L__R__R_", target = "L______RR"
Output: true
'''

# O(n) time | O(1) space
class Solution:
    def canChange(self, start: str, target: str) -> bool:
        sidx = 0

        for i, c in enumerate(target):

            if c == "_":
                continue

            while sidx < len(start) and start[sidx] == "_":
                sidx += 1

            if sidx == len(start):
                return False

            if start[sidx] != c:
                return False

            if c == "L" and i > sidx:
                return False

            elif c == "R" and i < sidx:
                return False

            sidx += 1

        while sidx < len(start):
            if start[sidx] != "_":
                return False

            sidx += 1

        return True
