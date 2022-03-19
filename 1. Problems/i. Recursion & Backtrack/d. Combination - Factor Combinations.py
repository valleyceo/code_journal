# LC 254. Factor Combinations

'''
Numbers can be regarded as the product of their factors.

For example, 8 = 2 x 2 x 2 = 2 x 4.
Given an integer n, return all possible combinations of its factors. You may return the answer in any order.

Note that the factors should be in the range [2, n - 1].

Example 1:

Input: n = 1
Output: []
Example 2:

Input: n = 12
Output: [[2,6],[3,4],[2,2,3]]
Example 3:

Input: n = 37
Output: []
'''
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:

        def backtrack(path, idx, rem):
            if len(path) > 0 and path[-1] <= rem:
                res.append(path + [rem])

            for i in range(idx, len(divs)):
                if rem % divs[i] == 0:
                    path.append(divs[i])
                    backtrack(path, i, rem // divs[i])
                    path.pop()

        res = []
        divs = self.getDivisors(n)
        backtrack([], 0, n)
        return res

    def getDivisors(self, n):
        divs = []

        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                divs.append(i)

        return divs
