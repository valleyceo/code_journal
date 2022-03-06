# 5. Longest Palindromic Substring

'''
Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.manacherSolution(s)

    def manacherSolution(self, s: str) -> str:
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i])
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > R:
                C, R = i, i + P[i]

        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]

    def nSqrSolution(self, s: str) -> str:
        maxLen = 0
        maxStrIdx = 0

        for i in range(len(s)):
            # odd string
            start = i - 1
            end = i

            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end-start+1 > maxLen:
                    maxLen = end-start + 1
                    maxStrIdx = start
                start -= 1
                end += 1

            # even string
            start = i
            end = i

            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end-start+1 > maxLen:
                    maxLen = end-start + 1
                    maxStrIdx = start

                start -= 1
                end += 1

        return s[maxStrIdx:maxStrIdx+maxLen]
