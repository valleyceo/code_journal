# 335. Self Crossing

'''
You are given an array of integers distance.

You start at point (0,0) on an X-Y plane and you move distance[0] meters to the north, then distance[1] meters to the west, distance[2] meters to the south, distance[3] meters to the east, and so on. In other words, after each move, your direction changes counter-clockwise.

Return true if your path crosses itself, and false if it does not.

Example 1:

Input: distance = [2,1,1,2]
Output: true

Example 2:

Input: distance = [1,2,3,4]
Output: false
'''
class Solution:
    # O(n) time | O(1) space
    def isSelfCrossing(self, d: List[int]) -> bool:
        if len(d) < 4:
            return False

        for i in range(3, len(d)):
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True

            if i >= 4:
                if d[i-1] == d[i-3] and d[i] + d[i-4] >= d[i-2]:
                    return True

            if i >= 5:
                if d[i-2] >= d[i-4] and d[i] >= d[i-2] - d[i-4] and \
                   d[i-3] >= d[i-1] and d[i-3] - d[i-5] <= d[i-1]:
                    return True

        return False

'''
3 Cases illustration (source: Leetcode@niwota)

                 i-2
    case 1 : i-1┌─┐
                └─┼─>i
                 i-3

                    i-2
    case 2 : i-1 ┌────┐
                 └─══>┘i-3
                 i  i-4      (i overlapped i-4)

    case 3 :    i-4
               ┌──┐
               │i<┼─┐
            i-3│ i-5│i-1
               └────┘
                i-2
'''
