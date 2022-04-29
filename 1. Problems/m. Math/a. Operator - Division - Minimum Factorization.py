# LC 625. Minimum Factorization

'''
Given a positive integer num, return the smallest positive integer x whose multiplication of each digit equals num. If there is no answer or the answer is not fit in 32-bit signed integer, return 0.

Example 1:

Input: num = 48
Output: 68

Example 2:

Input: num = 15
Output: 35
'''
class Solution:
    def smallestFactorization(self, num: int) -> int:
        return self.solution2(num)

    # O(8log(n)) time | O(1) space
    def solution1(self, num: int) -> int:
        if num == 1:
            return 1

        narr = []

        while num > 1:
            for d in range(9, 1, -1):
                if num % d == 0:
                    num //= d
                    narr.append(d)
                    break
            else:
                return 0

        res = int("".join(map(str, narr[::-1])))
        return res if res < 2**31 else 0

    # O(8log(n)) time | O(1) space
    def solution2(self, num: int) -> int:
        if num < 2:
            return num

        mult = 1
        res = 0

        for i in range(9, 1, -1):
            while num % i == 0:
                res += i * mult
                num //= i
                mult *= 10

        return res if num < 2 and res < 2**31 else 0
