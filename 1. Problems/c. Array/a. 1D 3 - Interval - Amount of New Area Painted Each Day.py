# LC 2158. Amount of New Area Painted Each Day

'''
There is a long and thin painting that can be represented by a number line. You are given a 0-indexed 2D integer array paint of length n, where paint[i] = [starti, endi]. This means that on the ith day you need to paint the area between starti and endi.

Painting the same area multiple times will create an uneven painting so you only want to paint each area of the painting at most once.

Return an integer array worklog of length n, where worklog[i] is the amount of new area that you painted on the ith day.
'''
from sortedcontainers import SortedList

class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        return self.RBTree(paint)

    def naiveDiscretizedTLE(self, paint: List[List[int]]) -> List[int]:
        dp = [False] * (5 * 10**4 + 1)
        res = []

        for s, e in paint:
            count = 0

            for i in range(s, e):
                if not dp[i]:
                    count += 1
                    dp[i] = True

            res.append(count)

        return res

    def discretizedSolution(self, paint: List[List[int]]) -> List[int]:
        dp = [-1] * (5 * 10**4 + 1)
        res = []

        for s, e in paint:
            count = 0
            idx = s

            while idx < e:
                if dp[idx] != -1:
                    idx = dp[idx]
                else:
                    count += 1
                    dp[idx] = e
                    idx += 1

            res.append(count)

        return res

    def RBTree(self, paint: List[List[int]]) -> List[int]:

        intervals = []
        max_pos = 0

        for i, [s, e] in enumerate(paint):
            intervals.append((s, i, 1))
            intervals.append((e, i, -1))
            max_pos = max(max_pos, e)

        intervals.sort()
        res = [0] * len(paint)
        idx_list = SortedList()
        i = 0

        for pos in range(max_pos + 1):
            while i < len(intervals) and intervals[i][0] == pos:
                pos, idx, flag = intervals[i]

                if flag == 1:
                    idx_list.add(idx)
                else:
                    idx_list.remove(idx)

                i += 1

            if idx_list:
                res[idx_list[0]] += 1

        return res
