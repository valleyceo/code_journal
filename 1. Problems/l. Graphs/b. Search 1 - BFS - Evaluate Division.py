# 399. Evaluate Division

'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation:
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= Cj.length, Dj.length <= 5
Ai, Bi, Cj, Dj consist of lower case English letters and digits.
'''
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        return self.bfs(equations, values, queries)

    def bfs(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        eqnDict = defaultdict(list)
        valDict = defaultdict(int)

        for eqn, val in zip(equations, values):
            eqnDict[eqn[0]] += [eqn[1]]
            eqnDict[eqn[1]] += [eqn[0]]
            valDict[(eqn[0], eqn[1])] = val
            valDict[(eqn[1], eqn[0])] = 1/val

        res = []
        for q in queries:
            res.append(self.getPath(q[0], q[1], eqnDict, valDict))

        return res

    def getPath(self, a, b, eqn, val) -> int:
        if a not in eqn:
            return -1

        que = [(a, 1)]
        s = set()

        while que:
            node = que.pop()
            s.add(node[0])

            if node[0] == b:
                return node[1]

            for n in eqn[node[0]]:
                if n in s:
                    continue

                que.append((n, node[1] * val[(node[0], n)]))

        return -1


'''
- Can solve using Union Find
'''
