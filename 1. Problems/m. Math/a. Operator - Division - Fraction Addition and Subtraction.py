# LC Fraction Addition and Subtraction

'''
Given a string expression representing an expression of fraction addition and subtraction, return the calculation result in string format.

The final result should be an irreducible fraction. If your final result is an integer, change it to the format of a fraction that has a denominator 1. So in this case, 2 should be converted to 2/1.

Example 1:

Input: expression = "-1/2+1/2"
Output: "0/1"

Example 2:

Input: expression = "-1/2+1/2+1/3"
Output: "1/3"

Example 3:

Input: expression = "1/3-1/2"
Output: "-1/6"
'''
from fractions import Fraction

class Solution:
    def fractionAddition(self, expression: str) -> str:
        return self.useGCD(expression)

    def useLibrary(self, expression: str) -> str:
        exp_arr = expression.replace("+", " +").replace("-", " -").split()
        f = sum(map(Fraction, exp_arr))

        return "{}/{}".format(f.numerator, f.denominator)

    def useRegex(self, expression: str) -> str:
        exp_arr = re.findall('[+-]?\d+/\d+', expression)
        f = sum(map(Fraction, exp_arr))

        return "{}/{}".format(f.numerator, f.denominator)

    def useGCD(self, expression: str) -> str:
        def gcd(m, n):
            while n != 0:
                m, n = n, m % n
            return m

        arr = map(int, re.findall('[+-]?\d+', expression))
        num = 0
        den = 1

        for next_num in arr:
            next_den = next(arr)
            num = num * next_den + den * next_num
            den *= next_den

            g = gcd(num, den)
            num //= g
            den //= g

        return "{}/{}".format(num, den)
