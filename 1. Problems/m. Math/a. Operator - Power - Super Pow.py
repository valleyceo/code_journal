# 372. Super Pow

'''
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

Example 1:

Input: a = 2, b = [3]
Output: 8

Example 2:

Input: a = 2, b = [1,0]
Output: 1024

Example 3:

Input: a = 1, b = [4,3,3,8,5,2]
Output: 1
'''
class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod = 1337
        dp = [0] * len(b)
        dp[0] = a % mod

        for i in range(1, len(b)):
            dp[i] = (dp[i - 1] ** 10) % 1337

        res = 1

        for val, count in zip(dp, b[::-1]):

            res *= val ** count
            res %= mod

        return res
