# LC 1345. Jump Game IV

'''
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.
'''

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)

        if n <= 1:
            return 0

        graph = defaultdict(list)

        for i, val in enumerate(arr):
            graph[val].append(i)

        queue1 = set([0])
        queue2 = set([n - 1])
        visited = {0, n - 1}
        step = 0

        while queue1:

            if len(queue1) > len(queue2):
                queue1, queue2 = queue2, queue1

            next_queue = set()

            for node in queue1:

                for child in graph[arr[node]]:
                    if child in queue2:
                        return step + 1

                    if child not in visited:
                        visited.add(child)
                        next_queue.add(child)

                graph[arr[node]].clear()

                for child in [node - 1, node + 1]:
                    if child in queue2:
                        return step + 1

                    if 0 <= child < n and child not in visited:
                        visited.add(child)
                        next_queue.add(child)

            queue1 = next_queue
            step += 1

        return -1
