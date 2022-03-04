# LC 20. Valid Parentheses

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
# O(n) time | O(n) space
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pmap = {")":"(", "]":"[","}":"{"}

        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif stack and c in pmap and pmap[c] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0

'''
- Note: Counter does not work. Case: "[(])"
'''
