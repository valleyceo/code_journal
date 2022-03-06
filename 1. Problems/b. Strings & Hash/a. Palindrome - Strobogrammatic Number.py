# LC 246. Strobogrammatic Number

'''
Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
'''

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        rotationDict = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        rotationNum = ""

        for c in reversed(num):
            if c not in rotationDict:
                return False

            rotationNum += rotationDict[c]

        if len(rotationNum) > 1 and rotationNum[0] == "0":
            return False

        return num == rotationNum
