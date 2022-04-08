# LC 2222. Number of Ways to Select Buildings

'''
You are given a 0-indexed binary string s which represents the types of buildings along a street where:

s[i] = '0' denotes that the ith building is an office and
s[i] = '1' denotes that the ith building is a restaurant.
As a city official, you would like to select 3 buildings for random inspection. However, to ensure variety, no two consecutive buildings out of the selected buildings can be of the same type.

For example, given s = "001101", we cannot select the 1st, 3rd, and 5th buildings as that would form "011" which is not allowed due to having two consecutive buildings of the same type.
Return the number of valid ways to select 3 buildings.
'''

class Solution:
    def numberOfWays(self, s: str) -> int:
        return self.slickSolution(s)

    # O(n) time | O(n) space
    def mySolution(self, s: str) -> int:
        dp_left = [[0, 0] for _ in range(len(s))]
        dp_right = [[0, 0] for _ in range(len(s))]

        for i in range(len(s)):
            if s[i] == '0':
                dp_left[i][0] += 1
            else:
                dp_left[i][1] += 1

            if i > 0:
                dp_left[i][0] += dp_left[i-1][0]
                dp_left[i][1] += dp_left[i-1][1]

        for i in range(len(s)-1, -1, -1):
            if s[i] == '0':
                dp_right[i][0] += 1
            else:
                dp_right[i][1] += 1

            if i < len(s) - 1:
                dp_right[i][0] += dp_right[i+1][0]
                dp_right[i][1] += dp_right[i+1][1]

        res = 0

        for i in range(1, len(s)-1):
            if s[i] == "0":
                res += dp_left[i-1][1] * dp_right[i+1][1]
            else:
                res += dp_left[i-1][0] * dp_right[i+1][0]

        return res

    # O(n) time | O(1) space
    def slickSolution(self, s: str) -> int:
        dp = defaultdict(int)

        for c in s:
            if c == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
            else:
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]

        return dp["010"] + dp["101"]
