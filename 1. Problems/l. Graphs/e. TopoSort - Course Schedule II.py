# 210. Course Schedule II

'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].

Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].

Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
'''
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = [0] * numCourses

        if numCourses == 0:
            return res

        if not prerequisites:
            return [i for i in range(numCourses)]

        inDegree = [0] * numCourses
        que = deque()

        for r in prerequisites:
            inDegree[r[0]] += 1

        for i in range(numCourses):
            if inDegree[i] == 0:
                que.append(i)

        if not que:
            return []

        idx = 0

        while que:
            course = que.popleft()
            res[idx] = course
            idx += 1

            for r in prerequisites:
                if r[1] == course:
                    inDegree[r[0]] -= 1
                    if inDegree[r[0]] == 0:
                        que.append(r[0])

        if any(i for i in inDegree):
            return []

        return res
