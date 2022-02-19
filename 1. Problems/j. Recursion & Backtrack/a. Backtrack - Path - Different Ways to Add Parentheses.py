# 241. Different Ways to Add Parentheses

'''
Given a string expression of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. You may return the answer in any order.

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0
(2-(1-1)) = 2

Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10

Constraints:
1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.
All the integer values in the input expression are in the range [0, 99].
'''

# O(N) time using caching | O(N) space
class Solution:
    @lru_cache(None)
    def diffWaysToCompute(self, exp: str) -> List[int]:
        if exp.isdigit():
            return [int(exp)]

        res = []

        for i in range(len(exp)):
            if exp[i] in "*+-":
                left = self.diffWaysToCompute(exp[:i])
                right = self.diffWaysToCompute(exp[i+1:])

                for l in left:
                    for r in right:
                        if exp[i] == "*":
                            res.append(l * r)
                        elif exp[i] == "+":
                            res.append(l + r)
                        elif exp[i] == "-":
                            res.append(l - r)

        return res
