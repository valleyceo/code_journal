# LC 1376. Time Needed to Inform All Employees

'''
A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.

Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.

The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.

The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).

Return the number of minutes needed to inform all the employees about the urgent news.
'''

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        return self.bottomUp(n, headID, manager, informTime)

    def topDown(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(list)

        for i, m in enumerate(manager):
            children[m].append(i)

        def dfs(node):
            max_val = 0

            for next_node in children[node]:
                max_val = max(max_val, dfs(next_node) + informTime[node])

            return max_val

        return dfs(headID)

    def bottomUp(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(idx):
            if manager[idx] != -1:
                informTime[idx] += dfs(manager[idx])
                manager[idx] = -1

            return informTime[idx]

        res = 0

        for i in range(n):
            res = max(res, dfs(i))

        return res
