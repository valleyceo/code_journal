# LC 214. Shortest Palindrome

'''
You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: s = "abcd"
Output: "dcbabcd"
'''
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        return self.KMP(s)

    def bruteForce(self, s: str) -> str:
        def isPalindrome(s1):
            l = 0
            r = len(s1) - 1

            while l < r:
                if s1[l] != s1[r]:
                    return False

                l += 1
                r -= 1

            return True

        for i in reversed(range(1, len(s) + 1)):
            if isPalindrome(s[:i]):
                rightStr = s[i:]
                return rightStr[::-1] + s

        return ""

    def twoPointers(self, s: str) -> str:
        n = len(s)
        i = 0

        for j in reversed(range(n)):
            if s[i] == s[j]:
                i += 1

        if i == n:
            return s

        remain = s[i:]

        return remain[::-1] + self.twoPointers(s[:i]) + remain

    def KMP(self, s: str) -> str:
        n = len(s)
        rev = s[::-1]
        s_new = s + "#" + rev
        n_new = len(s_new)
        dp = [0] * n_new

        for i in range(1, n_new):
            t = dp[i - 1]

            while t > 0 and s_new[i] != s_new[t]:
                t = dp[t - 1]

            if s_new[i] == s_new[t]:
                t += 1

            dp[i] = t

        return rev[: n - dp[-1]] + s
