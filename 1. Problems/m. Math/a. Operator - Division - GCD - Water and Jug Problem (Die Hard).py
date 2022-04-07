# 365. Water and Jug Problem

'''
You are given two jugs with capacities jug1Capacity and jug2Capacity liters. There is an infinite amount of water supply available. Determine whether it is possible to measure exactly targetCapacity liters using these two jugs.

If targetCapacity liters of water are measurable, you must have targetCapacity liters of water contained within one or both buckets by the end.

Operations allowed:

Fill any of the jugs with water.
Empty any of the jugs.
Pour water from one jug into another till the other jug is completely full, or the first jug itself is empty.

Example 1:

Input: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
Output: true
Explanation: The famous Die Hard example

Example 2:

Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
Output: false

Example 3:

Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
Output: true
'''
class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        return self.gcdSolution(jug1Capacity, jug2Capacity, targetCapacity)

    def bfs(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:

        def findNext(val, c1, c2):
            if val >= c1:
                return 0

            new_cap = c1 - val
            rem = new_cap % c2
            return c2 - rem

        if jug1Capacity > jug2Capacity:
            jug1Capacity, jug2Capacity = jug2Capacity, jug1Capacity

        visited = set([0, jug1Capacity, jug2Capacity, jug1Capacity + jug2Capacity])
        queue = [abs(jug1Capacity - (jug2Capacity % jug1Capacity))]

        while queue:
            next_val = queue.pop()

            if next_val in visited:
                continue

            visited.add(next_val)
            visited.add(next_val + jug1Capacity)
            visited.add(next_val + jug2Capacity)

            queue.append(findNext(next_val, jug1Capacity, jug2Capacity))
            queue.append(findNext(next_val, jug2Capacity, jug1Capacity))

        return targetCapacity in visited

    def gcdSolution(self, c1: int, c2: int, t: int) -> bool:
        def gcd(a, b):
            while b != 0:
                a, b = b, a % b

            return a

        if c1 + c2 < t:
            return False

        if c1 == t or c2 == t or c1 + c2 == t:
            return True

        return t % gcd(c1, c2) == 0
