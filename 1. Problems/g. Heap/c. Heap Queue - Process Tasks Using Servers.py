# LC 1882. Process Tasks Using Servers

'''
You are given two 0-indexed integer arrays servers and tasks of lengths n​​​​​​ and m​​​​​​ respectively. servers[i] is the weight of the i​​​​​​th​​​​ server, and tasks[j] is the time needed to process the j​​​​​​th​​​​ task in seconds.

Tasks are assigned to the servers using a task queue. Initially, all servers are free, and the queue is empty.

At second j, the jth task is inserted into the queue (starting with the 0th task being inserted at second 0). As long as there are free servers and the queue is not empty, the task in the front of the queue will be assigned to a free server with the smallest weight, and in case of a tie, it is assigned to a free server with the smallest index.

If there are no free servers and the queue is not empty, we wait until a server becomes free and immediately assign the next task. If multiple servers become free at the same time, then multiple tasks from the queue will be assigned in order of insertion following the weight and index priorities above.

A server that is assigned task j at second t will be free again at second t + tasks[j].

Build an array ans​​​​ of length m, where ans[j] is the index of the server the j​​​​​​th task will be assigned to.

Return the array ans​​​​.
'''
# O(s+t) time | O(s) space
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        res = []
        avail_queue = []
        proc_queue = []

        for i, w in enumerate(servers):
            avail_queue.append([w, i, 0])

        heapq.heapify(avail_queue)

        for curr_time, task in enumerate(tasks):
            while (proc_queue and proc_queue[0][0] <= curr_time) or not avail_queue:
                time, w, idx = heapq.heappop(proc_queue)
                heapq.heappush(avail_queue, [w, idx, time])

            weight, idx, time = heapq.heappop(avail_queue)
            res.append(idx)

            heapq.heappush(proc_queue, [max(time, curr_time) + task, weight, idx])

        return res
