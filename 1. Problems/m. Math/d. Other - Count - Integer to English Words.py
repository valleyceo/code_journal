# LC 273. Integer to English Words

'''
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
'''
# O(N) time, n digits | O(1) space
class Solution:
    def numberToWords(self, num: int) -> str:
        def twoDigit(n):
            if not n:
                return ""
            elif n < 10:
                return ones[n]
            elif n < 20:
                return teens[n]
            else:
                t = n // 10
                rest = n % 10
                return tens[t] + " " + ones[rest] if rest else tens[t]

        def threeDigit(n):
            h = n // 100
            rest = n % 100

            if h and rest:
                return ones[h] + " Hundred " + twoDigit(rest)
            elif h:
                return ones[h] + " Hundred"
            elif rest:
                return twoDigit(rest)

        ones = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four',
                5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}

        teens = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen'}

        tens = {2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty',
                7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}

        B = 1e9
        M = 1e6
        billion = num // B
        million = (num - billion * B) // M
        thousand = (num - billion * B - million * M) // 1000
        rest = num % 1000

        if not num:
            return "Zero"

        res = ""

        if billion:
            res = threeDigit(billion) + " Billion"

        if million:
            res += " " if res else ""
            res += threeDigit(million) + " Million"

        if thousand:
            res += " " if res else ""
            res += threeDigit(thousand) + " Thousand"

        if rest:
            res += " " if res else ""
            res += threeDigit(rest)

        return res
