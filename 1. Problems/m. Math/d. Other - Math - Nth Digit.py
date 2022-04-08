# LC 400. Nth Digit

'''
Given an integer n, return the nth digit of the infinite integer sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].

Example 1:

Input: n = 3
Output: 3

Example 2:

Input: n = 11
Output: 0
Explanation: The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
'''
# O(log(N)) time | O(1) space
class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        base = 1

        while n > 9 * base * digit:
            n -= 9 * base * digit
            digit += 1
            base *= 10

        div, mod = divmod(n - 1, digit)
        return int(str(base + div)[mod])


"""
NOTE:
- find nth from 123456789101112131415161718192021222324252627282930...

1-9 -> 9 -> 9 digit
10-99 -> 90 -> 90*2 digit
100-999 -> 900 -. 900*3 digit
"""
