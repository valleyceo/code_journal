# 247. Strobogrammatic Number II

'''
Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]

Constraints:
1 <= n <= 14
'''

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ["0", "1", "8"]

        rotNumber = {"0": "0","6": "9", "9": "6", "1": "1", "8": "8"}
        path = [("", "")]

        for _ in range(n//2):
            temp = []
            for l, r in path:
                for num, rnum in rotNumber.items():
                    if l == "" and num == "0":
                        continue

                    temp.append((l + num, r + rnum))
            path = temp

        res = []

        if n % 2 == 0:
            for l, r in path:
                res.append(l + r[::-1])
        else:
            for l, r in path:
                res.append(l + "0" + r[::-1])
                res.append(l + "1" + r[::-1])
                res.append(l + "8" + r[::-1])

        return res
