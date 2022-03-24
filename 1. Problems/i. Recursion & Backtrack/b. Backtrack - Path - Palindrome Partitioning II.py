# LC 132. Palindrome Partitioning II

'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Example 2:

Input: s = "a"
Output: 0

Example 3:

Input: s = "ab"
Output: 1
'''
class Solution:
    def minCut(self, s: str) -> int:
        return self.bottomUp(s)

    # O(n^2) time | O(n^2) space
    def bottomUp(self, s: str) -> int:
        pdp = [[False for _ in range(len(s))] for _ in range(len(s))]
        mincut_dp = [0] * len(s)

        for right in range(len(s)):
            minCut = right

            for left in range(right + 1):
                if s[left] == s[right] and ((right - left <= 2) or pdp[left + 1][right - 1]):
                    pdp[left][right] = True
                    minCut = 0 if left == 0 else min(minCut, mincut_dp[left - 1] + 1)

            mincut_dp[right] = minCut

        return mincut_dp[-1]
