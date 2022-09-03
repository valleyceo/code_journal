# LC 1363. Largest Multiple of Three

'''
Given an array of digits digits, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer return an empty string.

Since the answer may not fit in an integer data type, return the answer as a string. Note that the returning answer must not contain unnecessary leading zeros.
'''

class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        return self.mathSolution(digits)

    def DPSolution(self, digits: List[int]) -> str:
        dp = [-1, -1, -1]

        for n in sorted(digits)[::-1]:
            for x in dp + [0]:
                y = x * 10 + n
                dp[y % 3] = max(dp[y % 3], y)

        return str(dp[0]) if dp[0] >= 0 else ""

    def mathSolution(self, digits: List[int]) -> str:
        total = sum(digits)
        count = Counter(digits)
        digits.sort(reverse = True)

        def f(idx):
            if count[idx]:
                digits.remove(idx)
                count[idx] -= 1

            if not digits:
                return ""

            if not any(digits):
                return "0"

            if sum(digits) % 3 == 0:
                return "".join(map(str, digits))

        if total % 3 == 0:
            return f(-1)

        if total % 3 == 1 and count[1] + count[4] + count[7]:
            return f(1) or f(4) or f(7)

        if total % 3 == 2 and count[2] + count[5] + count[8]:
            return f(2) or f(5) or f(8)

        if total % 3 == 2:
            return f(1) or f(1) or f(4) or f(4) or f(7) or f(7)

        return f(2) or f(2) or f(5) or f(5) or f(8) or f(8)
