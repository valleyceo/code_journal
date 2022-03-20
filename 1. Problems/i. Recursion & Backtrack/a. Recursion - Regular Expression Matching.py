# LC 10. Regular Expression Matching

'''
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Example 1:

Input: s = "aa", p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: s = "aa", p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input: s = "ab", p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
'''
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.bottomUp(s, p)

    # O(NM) time | O(NM) space
    def bottomUp(self, text: str, pattern: str) -> bool:
        dp = [[False] * (len(pattern) + 1) for _ in range(len(text) + 1)]
        dp[-1][-1] = True
        print(dp)
        for i in range(len(text), -1, -1):
            for j in range(len(pattern) - 1, -1, -1):

                first_match = i < len(text) and pattern[j] in {text[i], '.'}

                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or first_match and dp[i + 1][j]
                else:
                    dp[i][j] = first_match and dp[i + 1][j + 1]

        return dp[0][0]

    # O(NM) time | O(NM) space
    def topDown(self, text: str, pattern: str) -> bool:
        @lru_cache(None)
        def recursion(i: int, j: int) -> bool:
            if j == len(pattern):
                res = i == len(text)
            else:
                first_match = i < len(text) and pattern[j] in {text[i], '.'}

                if j + 1 < len(pattern) and pattern[j + 1] == "*":
                    res = recursion(i, j + 2) or first_match and recursion(i + 1, j)
                else:
                    res = first_match and recursion(i + 1, j + 1)

            return res

        return recursion(0, 0)


    def mytopDown(self, s: str, p: str) -> bool:

        @lru_cache(None)
        def recursion(sidx: int, pidx: int) -> bool:
            if sidx == len(s) and pidx == len(p):
                return True

            if sidx > len(s) or pidx >= len(p):
                return False

            flag = False

            if pidx + 1 < len(p) and p[pidx + 1] == "*":
                if p[pidx] == ".":
                    flag |= recursion(sidx, pidx + 2)
                    flag |= recursion(sidx + 1, pidx)
                else:
                    if sidx < len(s) and s[sidx] == p[pidx]:
                        flag |= recursion(sidx + 1, pidx)
                        flag |= recursion(sidx, pidx + 2)
                    else:
                        flag |= recursion(sidx, pidx + 2)
            elif p[pidx] == ".":
                flag |= recursion(sidx + 1, pidx + 1)
            else:
                if sidx < len(s) and p[pidx] == s[sidx]:
                    flag |= recursion(sidx + 1, pidx + 1)
                else:
                    return False

            return flag

        return recursion(0, 0)
