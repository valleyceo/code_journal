# LC 772. Basic Calculator III

'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, '+', '-', '*', '/' operators, and open '(' and closing parentheses ')'. The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

Example 1:

Input: s = "1+1"
Output: 2
Example 2:

Input: s = "6-4/2"
Output: 4
Example 3:

Input: s = "2*(5+5*2)/3+(6/2+8)"
Output: 21
'''

# O(n) time | O(n) space
class Solution:
    def calculate(self, s: str) -> int:
        return self.recursiveSolution(s)

    def recursiveSolution(self, s: str) -> int:

        def evaluate():
            nonlocal i

            stack = []
            curr_val = 0
            op = "+"

            while i < len(s):
                char = s[i]

                if char.isdigit():
                    curr_val = curr_val * 10 + int(char)
                elif char == "(":
                    i += 1
                    curr_val = evaluate()

                if char in "+-*/" or i == len(s) - 1 or char == ")":
                    if op == "+":
                        stack.append(curr_val)
                    elif op == "-":
                        stack.append(-curr_val)
                    elif op == "*":
                        stack.append(curr_val * stack.pop())
                    elif op == "/":
                        stack.append(int(stack.pop() / curr_val))

                    curr_val = 0
                    op = char

                    if char == ")":
                        break

                i += 1

            res = 0

            while stack:
                res += stack.pop()

            return res

        i = 0
        return evaluate()
