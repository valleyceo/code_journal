# LC 475. Heaters

'''
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range.

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that those heaters could cover all houses.

Notice that all the heaters follow your radius standard, and the warm radius will the same.

Example 1:

Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

Example 2:

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.

Example 3:

Input: houses = [1,5], heaters = [2]
Output: 3
'''

import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        return self.bisectSolution(houses, heaters)

    # O(N + M) time | O(N + M) space 4 sorted arrahy
    def onePassSolution(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        hIdx = 0
        max_dist = 0

        for h in houses:
            while hIdx + 1 < len(heaters) and abs(heaters[hIdx + 1] - h) <= abs(heaters[hIdx] - h):
                hIdx += 1

            max_dist = max(max_dist, abs(heaters[hIdx] - h))

        return max_dist

    # O(nlogn + mlogm) time | O(m + n) space
    def bisectSolution(self, houses: List[int], heaters: List[int]) -> int:
        heaters = [float("-inf")] + sorted(heaters) + [float("inf")]
        houses.sort()
        res = 0

        for h in houses:
            min_idx = bisect.bisect(heaters, h)
            min_dist = min(abs(heaters[min_idx]-h), abs(heaters[min_idx-1]-h))
            res = max(res, min_dist)

        return res
