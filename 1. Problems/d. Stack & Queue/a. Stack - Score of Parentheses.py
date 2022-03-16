# LC 856. Score of Parentheses

'''
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:

Input: s = "()"
Output: 1

Example 2:

Input: s = "(())"
Output: 2

Example 3:

Input: s = "()()"
Output: 2
'''
# O(n) time | O(n) space
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                val = stack.pop()
                stack[-1] += max(1, val * 2)

        return stack.pop()
