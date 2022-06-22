# LC 224. Basic Calculator

'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1 + 1"
Output: 2

Example 2:

Input: s = " 2-1 + 2 "
Output: 3

Example 3:

Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        val = 0
        res = 0
        sign = 1

        for c in s:
            if c.isdigit():
                val = val * 10 + int(c)
            elif c in "-+":
                res += sign * val
                val = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif c == ")":
                res += sign * val
                res *= stack.pop()
                res += stack.pop()
                val = 0

        return res + val * sign
