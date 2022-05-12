# LC 552. Student Attendance Record II

'''
An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
Any student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

Example 1:

Input: n = 2
Output: 8
Explanation: There are 8 records with length 2 that are eligible for an award:
"PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

Example 2:

Input: n = 1
Output: 3
Example 3:

Input: n = 10101
Output: 183236316
'''
class Solution:
    def checkRecord(self, n: int) -> int:
        return self.matrixExponentialSolution(n)

    # O(2*3*N) time | O(2*3*N) space
    # Memory limit exceed due to large recursion
    def topDown(self, n: int) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def backtrack(idx, absent, late):
            if idx > n:
                return 0

            if idx == n:
                return 1

            count = backtrack(idx + 1, absent, 0)

            if absent == 0:
                count += backtrack(idx + 1, 1, 0) % mod

            if late < 2:
                count += backtrack(idx + 1, absent, late + 1) % mod

            return count

        return backtrack(0, 0, 0) % mod

    # O(n) time | O(n) space
    def bottomUp(self, n: int) -> int:
        mod = 10**9 + 7
        dp = [[[0] * 2 for _ in range(3)] for _ in range(n + 1)]
        dp[-1] = [[1] * 2 for _ in range(3)]

        for i in range(n - 1, -1, -1):
            for l in range(3):
                for a in range(2):
                    count = dp[i+1][0][a]

                    if a == 0:
                        count = (count + dp[i+1][0][1]) % mod

                    if l < 2:
                        count = (count + dp[i+1][l+1][a]) % mod

                    dp[i][l][a] = count % mod

        return dp[0][0][0]

    # O(n) time | O(1) space
    def bottomUpConst(self, n: int) -> int:
        mod = 10**9 + 7
        prev = [[1] * 2 for _ in range(3)]

        for i in range(n - 1, -1, -1):
            curr = [[0] * 2 for _ in range(3)]

            for l in range(3):
                for a in range(2):
                    count = prev[0][a]

                    if a == 0:
                        count = (count + prev[0][1]) % mod

                    if l < 2:
                        count = (count + prev[l+1][a]) % mod

                    curr[l][a] = count

            prev = curr

        return curr[0][0]

    # O(log(n)) time | O(1) space
    def matrixExponentialSolution(self, n: int) -> int:

        mod = 10**9 + 7
        M = [[0, 0, 1, 0, 0, 0],
             [1, 0, 1, 0, 0, 0],
             [0, 1, 1, 0, 0, 0],
             [0, 0, 1, 0, 0, 1],
             [0, 0, 1, 1, 0, 1],
             [0, 0, 1, 0, 1, 1]]
        size = len(M)

        def matMult(A, B):
            new_M = [[0] * size for _ in range(size)]

            for i in range(size):
                for j in range(size):
                    for k in range(size):
                        new_M[i][j] = (new_M[i][j] + A[i][k] * B[k][j]) % mod

            return new_M

        def matPower(A, p):
            res = [[0] * size for _ in range(size)]

            for i in range(size):
                res[i][i] = 1

            while p:
                if p & 1:
                    res = matMult(res, A)

                A = matMult(A, A)
                p >>= 1

            return res

        return matPower(M, n + 1)[5][2]
