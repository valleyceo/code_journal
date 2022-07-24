# LC 2188. Minimum Time to Finish the Race

'''
You are given a 0-indexed 2D integer array tires where tires[i] = [fi, ri] indicates that the ith tire can finish its xth successive lap in fi * ri(x-1) seconds.

For example, if fi = 3 and ri = 2, then the tire would finish its 1st lap in 3 seconds, its 2nd lap in 3 * 2 = 6 seconds, its 3rd lap in 3 * 22 = 12 seconds, etc.
You are also given an integer changeTime and an integer numLaps.

The race consists of numLaps laps and you may start the race with any tire. You have an unlimited supply of each tire and after every lap, you may change to any given tire (including the current tire type) if you wait changeTime seconds.

Return the minimum time to finish the race.
'''

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        return self.topDownSolution(tires, changeTime, numLaps)

    def topDownSolution(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:

        tires.sort()
        min_r = float('inf')
        f_tires = []

        for f, r in tires:
            if r < min_r:
                f_tires.append((f, r))
                min_r = r

        tires = f_tires

        @lru_cache(None)
        def solve(laps):
            res = float('inf')

            for f, r in tires:
                cost = 0

                for x in range(1, 16):
                    if x > laps:
                        break

                    cost += f * r**(x - 1)

                    if laps == x:
                        res = min(res, cost)
                    else:
                        res = min(res, cost + changeTime + solve(laps - x))

            return res

        return solve(numLaps)
