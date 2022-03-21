# LC 32. Longest Valid Parentheses

'''
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        res = 0
        op = cl = 0

        for c in s:
            if c == '(':
                op += 1
            else:
                cl += 1

            if op == cl:
                res = max(res, 2 * op)
            elif cl > op:
                cl = 0
                op = 0

        op = cl = 0

        for c in s[::-1]:
            if c == ')':
                op += 1
            else:
                cl += 1

            if op == cl:
                res = max(res, 2 * op)
            elif cl > op:
                cl = 0
                op = 0

        return res
