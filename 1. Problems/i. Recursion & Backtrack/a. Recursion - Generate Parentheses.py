# 22. Generate Parentheses

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]

Constraints:
1 <= n <= 8
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.recurse(n, 0, "", res)

        return res

    def recurse(self, n: int, o: int, s: str, res: List[str]) -> None:
        if n < 0:
            return

        if n == 0 and o == 0:
            res.append(s)
            return

        if o > 0:
            self.recurse(n, o-1, s + ")", res)
        self.recurse(n-1, o+1, s + "(", res)
        
