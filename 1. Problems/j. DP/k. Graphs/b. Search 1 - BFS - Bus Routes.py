# LC 815. Bus Routes

'''
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
'''

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        rset = [set(route) for route in routes]
        mp = defaultdict(list)
        graph = defaultdict(set)

        for i, route in enumerate(routes):
            for n in route:
                mp[n].append(i)

        for i in range(len(rset)):
            for j in range(i + 1, len(rset)):

                for n in rset[i]:
                    if n in rset[j]:
                        graph[i].add(j)
                        graph[j].add(i)

        queue = deque([n, 1] for n in mp[source])
        destination = set(mp[target])
        visited = set()

        while queue:
            idx, step = queue.popleft()
            visited.add(idx)

            if idx in destination:
                return step

            for next_idx in graph[idx]:
                if next_idx in visited:
                    continue

                queue.append([next_idx, step + 1])

        return -1
