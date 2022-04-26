# LC 2251. Number of Flowers in Full Bloom

'''
You are given a 0-indexed 2D integer array flowers, where flowers[i] = [starti, endi] means the ith flower will be in full bloom from starti to endi (inclusive). You are also given a 0-indexed integer array persons of size n, where persons[i] is the time that the ith person will arrive to see the flowers.

Return an integer array answer of size n, where answer[i] is the number of flowers that are in full bloom when the ith person arrives.
'''
from sortedcontainers import SortedDict

# O(nlogn + mlogn) time | O(n) space, n is the length of flowers, m is the length of persons
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        return self.diffSolution(flowers, persons)

    def searchSolution(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        start = sorted(a for a, b in flowers)
        end = sorted(b for a, b in flowers)
        res = []

        for p in persons:
            l = bisect_right(start, p)
            r = bisect_left(end, p)

            res.append(l - r)

        return res

    def diffSolution(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        diff = SortedDict({0:0})

        for i, j in flowers:
            diff[i] = diff.get(i, 0) + 1
            diff[j + 1] = diff.get(j + 1, 0) - 1

        count = list(accumulate(diff.values()))
        res = []

        for p in persons:
            idx = diff.bisect(p)
            res.append(count[idx - 1])

        return res
