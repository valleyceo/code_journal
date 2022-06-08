# LC 647. Palindromic Substrings

'''
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.manacherSolution(s)

    # O(n^2) time | O(n^2) space
    def dpSolution(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        res = 0

        for i in range(n):
            dp[i][i] = True
            res += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                res += 1

        for l in range(3, n + 1):
            for left in range(n - l + 1):
                right = left + l - 1
                dp[left][right] = dp[left + 1][right - 1] and s[left] == s[right]
                res += dp[left][right]

        return res

    # O(n) time | O(n) space
    def manacherSolution(self, string: str) -> int:

        def manacher(s):
            ms = "@#" + "#".join(s) + "#$"
            dp = [0] * len(ms)
            center = 0
            right = 0

            for i in range(1, len(ms) - 1):
                if i < right:
                    dp[i] = min(right - i, dp[2 * center - i]) # i' = C - (i - C)

                while ms[i + dp[i] + 1] == ms[i - dp[i] - 1]:
                    dp[i] += 1

                if i + dp[i] > right:
                    center = i
                    right = i + dp[i]

            return dp

        res = 0

        for l in manacher(string):
            res += (l + 1) // 2

        return res
