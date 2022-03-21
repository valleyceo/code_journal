# LC 65. Valid Number

'''
A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

Input: s = "0"
Output: true

Example 2:

Input: s = "e"
Output: false

Example 3:

Input: s = "."
Output: false
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.lower()
        esplit = s.split("e")

        for si in esplit:
            if si == "":
                return False

        if len(esplit) > 2:
            return False
        elif len(esplit) == 2:
            left, right = esplit

            if left[0] in "+-":
                left = left[1:]

            if right[0] in "+-":
                right = right[1:]

            return self.isValidInt(left) and self.isValidFloat(right)
        else:
            strval = esplit[0]

            if strval[0] in "+-":
                strval = strval[1:]

            return self.isValidFloat(strval)

    def isValidInt(self, s) -> bool:

        for c in s:
            if not c.isdigit():
                return False

        return True

    def isValidFloat(self, s) -> bool:

        if "." in s:
            ssplit = s.split(".")

            if len(ssplit) > 2:
                return False

            left, right = ssplit

            return self.isValidInt(left) and self.isValidInt(right)
        else:
            return self.isValidInt(s)
