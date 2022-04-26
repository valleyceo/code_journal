# LC 516. Longest Palindromic Subsequence

'''
Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        return self.bottomUp1D(s)

    # O(N^2) time | O(N^2) space
    def topDown(self, s: str) -> int:
        @lru_cache(None)
        def helper(left, right):
            if left == right:
                return 1

            elif left > right:
                return 0

            if s[left] == s[right]:
                return helper(left + 1, right - 1) + 2

            return max(helper(left + 1, right) , helper(left, right - 1))

        return helper(0, len(s) - 1)

    def bottomUp(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][-1]

    def bottomUp1D(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n)]
        prev = [0 for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i] = 1

            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[j] = prev[j - 1] + 2
                else:
                    dp[j] = max(prev[j], dp[j - 1])

            dp, prev = prev, dp

        return prev[-1]
