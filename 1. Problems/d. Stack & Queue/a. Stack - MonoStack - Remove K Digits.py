# LC 402. Remove K Digits

'''
Given string num representing a non-negative integer num, and an integer k, return the smallest possible integer after removing k digits from num.

Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
'''
# O(n) time | O(n) space
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for n in num:
            while k and stack and stack[-1] > n:
                stack.pop()
                k -= 1

            stack.append(n)

        res = stack[:-k] if k else stack

        return "".join(res).lstrip("0") or "0"
