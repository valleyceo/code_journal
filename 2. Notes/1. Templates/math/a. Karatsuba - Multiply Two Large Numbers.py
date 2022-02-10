# Multiply two numbers

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