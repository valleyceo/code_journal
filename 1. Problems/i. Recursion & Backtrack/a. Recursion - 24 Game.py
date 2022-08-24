# 679. 24 Game

'''
You are given an integer array cards of length 4. You have four cards, each containing a number in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.
'''

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        if len(cards) == 1:
            return abs(cards[0] - 24) < 0.1

        for i, a in enumerate(cards):
            for j, b in enumerate(cards):
                if i == j:
                    continue

                rem = []

                for k in range(len(cards)):
                    if k != i and k != j:
                        rem.append(cards[k])

                for x in [a + b, a - b, a * b, b and a / b]:
                    if self.judgePoint24(rem + [x]):
                        return True

        return False
