# LC 564. Find the Closest Palindrome

"""
Given a string n representing an integer, return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

Example 1:

Input: n = "123"
Output: "121"

Example 2:

Input: n = "1"
Output: "0"
Explanation: 0 and 2 are the closest palindromes but we return the smallest which is 0.
"""

class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if n == "1":
            return "0"

        nleft = (len(n) + 1) // 2
        pref = n[:nleft]

        if len(n) % 2 == 0:
            p1 = int(pref + pref[::-1])
        else:
            p1 = int(pref + pref[:-1][::-1])

        pref_m = str(int(pref) - 1)
        if len(pref_m) != len(pref) or pref_m == "0": # case "10" -> "9" or "1" -> "0"
            p2 = int("9" * (len(n) - 1))
        else:
            if len(n) % 2 == 0:
                p2 = int(pref_m + pref_m[::-1])
            else:
                p2 = int(pref_m + pref_m[:-1][::-1])

        pref_p = str(int(pref) + 1)

        if len(pref_p) != len(pref):
            p3 = 10 ** len(n) + 1
        else:
            if len(n) % 2 == 0:
                p3 = int(pref_p + pref_p[::-1])
            else:
                p3 = int(pref_p + pref_p[:-1][::-1])

        res = ""
        diff = float('inf')

        for p in [p2, p1, p3]:
            if abs(int(n) - p) < diff and str(p) != n:
                diff = abs(int(n) - p)
                res = str(p)

        return res
