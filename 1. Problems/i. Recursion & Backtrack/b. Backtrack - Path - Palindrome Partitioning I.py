# LC 131. Palindrome Partitioning

'''
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]
'''
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(idx, path):
            nonlocal res, dp

            if idx >= len(s):
                res.append(path[:])

            for i in range(idx, len(s)):
                if s[idx] == s[i] and (i - idx <= 2 or dp[idx+1][i-1]):
                    dp[idx][i] = True
                    path.append(s[idx:i+1])
                    dfs(i + 1, path)
                    path.pop()

        dp = [[False for _ in range(len(s))] for _ in range(len(s))]
        res = []
        dfs(0, [])
        return res
