# LC 878. Nth Magical Number

'''
A positive integer is magical if it is divisible by either a or b.

Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

Example 1:

Input: n = 1, a = 2, b = 3
Output: 2

Example 2:

Input: n = 4, a = 2, b = 3
Output: 6
'''

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        return self.binarySearch(n, a, b)

    def naiveTLE(self, n: int, a: int, b: int) -> int:
        res = 1
        num = 1
        mod = 10**9 + 7

        while n:
            if num % a == 0 or num % b == 0:
                n -= 1
                res = num

            num += 1

        return res % mod

    # O(A + B) time | O(1) space
    def mathSolution(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7

        L = a / gcd(a, b) * b
        M = L / a + L / b - 1

        q, r = divmod(n, M)

        if r == 0:
            return int(q * L) % mod

        heads = [a, b]

        for _ in range(int(r) - 1):
            if heads[0] < heads[1]:
                heads[0] += a
            else:
                heads[1] += b


        return int(q * L + min(heads)) % mod

    # O(log(N * min(a, b))) time | O(1) space
    def binarySearch(self, n: int, a: int, b: int) -> int:
        mod = 10**9 + 7
        L = a * b // gcd(a, b)

        def divCountBelow(x):
            return x//a + x//b - x//L

        low = 0
        high = n * min(a, b)

        while low < high:
            mid = (low + high) // 2

            if divCountBelow(mid) < n:
                low = mid + 1
            else:
                high = mid

        return low % mod
