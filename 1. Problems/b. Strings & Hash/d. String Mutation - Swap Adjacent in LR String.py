# 777. Swap Adjacent in LR String

'''
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example 1:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: true
Explanation: We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
Example 2:

Input: start = "X", end = "L"
Output: false
'''
# O(n) time | O(1) space
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if start.count('X') != end.count('X'):
            return False

        n = len(start)
        sidx = eidx = 0

        while sidx < n and eidx < n:
            if start[sidx] == 'X':
                sidx += 1
                continue

            if end[eidx] == "X":
                eidx += 1
                continue

            if start[sidx] != end[eidx]:
                return False

            # start[sidx] == end[eidx], but for "L" sidx needs to come later and "R" sooner
            if start[sidx] == "L" and sidx < eidx:
                return False

            if start[sidx] == "R" and sidx > eidx:
                return False

            sidx += 1
            eidx += 1

        return True
