# 233. Number of Digit One

'''
Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example 1:

Input: n = 13
Output: 6

Example 2:

Input: n = 0
Output: 0
'''
class Solution:
    def countDigitOne(self, n: int) -> int:
        res = 0
        i = 1

        while i <= n:
            divider = i * 10

            div = (n // divider) * i
            rem = n % divider - i + 1
            res += div + min(max(rem, 0), i)
            i *= 10

        return res

'''
Note:
- Mathematical derivation for each position

1s:
- 0~9 (1 ones)
- ~20 (2 ones)
- ~160 (16 ones)
- ~16x, x >= 1 (17 ones)

10s:
- ~100 (10 ones)
- ~1600 (160 ones)
- ~1610 (161 ones)
- ~161x, x > 0 (160 + x ones)
- ~1650 (160 + 10 ones) -> see that ones are capped after 1620
'''
