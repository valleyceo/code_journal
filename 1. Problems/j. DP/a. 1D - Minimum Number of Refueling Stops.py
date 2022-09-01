# LC 871. Minimum Number of Refueling Stops

'''
A car travels from a starting position to a destination which is target miles east of the starting position.

There are gas stations along the way. The gas stations are represented as an array stations where stations[i] = [positioni, fueli] indicates that the ith gas station is positioni miles east of the starting position and has fueli liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel liters of fuel in it. It uses one liter of gas per one mile that it drives. When the car reaches a gas station, it may stop and refuel, transferring all the gas from the station into the car.

Return the minimum number of refueling stops the car must make in order to reach its destination. If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can still refuel there. If the car reaches the destination with 0 fuel left, it is still considered to have arrived.
'''

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        return self.heapSolution(target, startFuel, stations)

    # O(n^2) time | O(n) space
    def naiveSolution(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        n = len(stations)
        dp = [startFuel] + [0] * n

        for i, (pos, fuel) in enumerate(stations):
            for j in range(i, -1, -1):
                if dp[j] >= pos:
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)

        for i, d in enumerate(dp):
            if d >= target:
                return i

        return -1

    # O(nlogn) time | O(n) space
    def heapSolution(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        q = []
        stations.append([target, float('inf')])

        res = 0
        prev = 0
        tank = startFuel

        for pos, fuel in stations:
            tank -= pos - prev

            while q and tank < 0:
                tank += -heapq.heappop(q)
                res += 1

            if tank < 0:
                return -1

            heapq.heappush(q, -fuel)
            prev = pos

        return res
