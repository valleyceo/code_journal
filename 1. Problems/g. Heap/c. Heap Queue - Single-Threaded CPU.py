# LC 1834. Single-Threaded CPU

'''
You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
'''
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        return self.solution2(tasks)

    def solution1(self, tasks: List[List[int]]) -> List[int]:
        task_list = []

        for i, task in enumerate(tasks):
            task_list.append([task[0], task[1], i])

        task_list.sort()
        curr_time = task_list[0][0]
        queue = []
        res = []
        i = 0

        while len(res) < len(task_list):

            while (i < len(task_list)) and (task_list[i][0] <= curr_time):
                heapq.heappush(queue, (task_list[i][1], task_list[i][2]))
                i += 1

            if queue:
                duration, idx = heapq.heappop(queue)
                curr_time += duration
                res.append(idx)

            elif i < len(task_list):
                curr_time = task_list[i][0]

        return res

    def solution2(self, tasks: List[List[int]]) -> List[int]:
        task_list = []

        for i, task in enumerate(tasks):
            task_list.append([task[0], task[1], i])

        task_list.sort()
        queue = []
        curr_time = 0
        res = []

        for time, duration, idx in task_list:
            while queue and curr_time < time:
                next_duration, next_idx = heapq.heappop(queue)
                curr_time += next_duration
                res.append(next_idx)

            curr_time = max(curr_time, time)
            heapq.heappush(queue, [duration, idx])

        while queue:
            next_duration, next_idx = heapq.heappop(queue)
            res.append(next_idx)

        return res
