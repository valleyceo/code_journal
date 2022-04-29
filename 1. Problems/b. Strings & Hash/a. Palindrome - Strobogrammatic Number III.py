# LC 248. Strobogrammatic Number III

'''
Given two strings low and high that represent two integers low and high where low <= high, return the number of strobogrammatic numbers in the range [low, high].

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: low = "50", high = "100"
Output: 3

Example 2:

Input: low = "0", high = "0"
Output: 1
'''
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        mp = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}

        ll = len(low)
        lh = len(high)

        if ll > lh or (ll == lh and low > high):
            return 0

        sarr = ["", "0", "1", "8"] # Center can be nothing (11, 9966) or 0,1,8 (181, 986)
        res = 0

        while sarr:
            temp = []

            for s in sarr:
                if len(s) < lh or (len(s) == lh and s <= high):
                    if len(s) > ll or (len(s) == ll and s >= low):
                        if not (len(s) > 1 and s[0] == "0"): # "0xx" is not counted
                            res += 1

                    if lh - len(s) >= 2:
                        for k in mp:
                            temp.append(k + s + mp[k])

            sarr = temp

        return res
