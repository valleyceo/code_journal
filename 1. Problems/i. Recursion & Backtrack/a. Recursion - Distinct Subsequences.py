# 115. Distinct Subsequences

'''
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        return self.bottomUp(s, t)

    def topDown(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        @lru_cache(None)
        def recursion(idx_s, idx_t):

            if idx_t == nt:
                return 1

            count = 0

            for i in range(idx_s, ns - (nt - idx_t - 1)):
                if s[i] == t[idx_t]:
                    count += recursion(i + 1, idx_t + 1)

            return count

        return recursion(0, 0)

    def bottomUp(self, s: str, t: str) -> int:
        ns = len(s)
        nt = len(t)

        dp = [[0 for _ in range(ns + 1)] for _ in range(nt + 1)]

        for i in range(ns):
            dp[0][i] = 1

        for i in range(1, nt + 1):
            for j in range(1, ns + 1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

        return dp[nt][ns]
