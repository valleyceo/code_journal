# LC 678. Valid Parenthesis String

'''
Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "(*)"
Output: true

Example 3:

Input: s = "(*))"
Output: true

Constraints:
1 <= s.length <= 100
s[i] is '(', ')' or '*'.
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        return self.topDown(s)

    # O(N) time | O(1) space
    def onePass(self, s: str, stack = [], cache = {}) -> bool:
        minOpen = 0
        maxOpen = 0

        for c in s:
            if c == "(":
                minOpen += 1
                maxOpen += 1
            elif c == "*":
                minOpen = max(minOpen - 1, 0)
                maxOpen += 1
            else:
                minOpen = max(minOpen - 1, 0)
                maxOpen -= 1

            if maxOpen < 0:
                return False

        return minOpen == 0

    # O(3*N) time | O(3*N) space
    def topDown(self, s: str, stack = [], cache = {}) -> bool:
        if not s and not stack: return True
        if not s and stack: return False

        key = s + ',' + ''.join(stack)
        if key in cache: return cache[ key ]

        if s[0] == '(':
            cache[ key ] = self.topDown(s[1:], stack + ['('], cache)
            return cache[ key ]

        if s[0] == ')' and stack:
            cache[ key ] = self.topDown(s[1:], stack[:-1], cache)
            return cache[ key ]
        elif s[0] == ')':
            return False

        empty = self.topDown(s[1:], stack, cache)
        Open = self.topDown(s[1:], stack + ['('], cache)
        Close = self.topDown(s[1:], stack[:-1], cache)

        cache[ key ] = empty or Open or Close
        return cache[ key ]

    # O(N^3) time | O(N^2) space
    def bottomUp(self, s):
        if not s: return True
        LEFTY, RIGHTY = '(*', ')*'

        n = len(s)
        dp = [[False] * n for _ in s]

        # Solve Dist 1
        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True
            if i < n-1 and s[i] in LEFTY and s[i+1] in RIGHTY:
                dp[i][i+1] = True

        # Solve Dist 1 - n
        for size in range(2, n):
            for i in range(n - size):
                if s[i] == '*' and dp[i+1][i+size]:
                    dp[i][i+size] = True
                elif s[i] in LEFTY:
                    for k in range(i+1, i+size+1):
                        if (s[k] in RIGHTY and
                                (k == i+1 or dp[i+1][k-1]) and
                                (k == i+size or dp[k+1][i+size])):
                            dp[i][i+size] = True

        return dp[0][-1]

    # O(N * 3^N) time | O(N) space
    def bruteForce(self, s):
        if not s: return True
        A = list(s)
        self.ans = False

        def solve(i):
            if i == len(A):
                self.ans |= valid()
            elif A[i] == '*':
                for c in '() ':
                    A[i] = c
                    solve(i+1)
                    if self.ans: return
                A[i] = '*'
            else:
                solve(i+1)

        def valid():
            bal = 0
            for x in A:
                if x == '(': bal += 1
                if x == ')': bal -= 1
                if bal < 0: break
            return bal == 0

        solve(0)
        return self.ans
