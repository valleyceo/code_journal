# LC 43. Multiply Strings

'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(self.karatsuba(num1, num2))

    def karatsuba(self, x: str, y: str) -> int:
        if len(x) == 1 or len(y) == 1:
            return int(x) * int(y)

        n = max(len(x), len(y))
        half = n // 2

        xl = x[:-half]
        xr = x[-half:]
        yl = y[:-half]
        yr = y[-half:]

        xl = xl if xl != "" else "0"
        xr = xr if xr != "" else "0"
        yl = yl if yl != "" else "0"
        yr = yr if yr != "" else "0"

        xlyl = self.karatsuba(xl, yl)
        xryr = self.karatsuba(xr, yr)
        mid = self.karatsuba(str(int(xl) + int(xr)), str(int(yl) + int(yr))) - xlyl - xryr

        return xlyl * 10**(2*half) + (mid * 10**half) + xryr
