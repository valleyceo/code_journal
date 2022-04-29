# LC 828. Count Unique Characters of All Substrings of a Given String

'''
Let's define a function countUniqueChars(s) that returns the number of unique characters on s.

For example, calling countUniqueChars(s) if s = "LEETCODE" then "L", "T", "C", "O", "D" are the unique characters since they appear only once in s, therefore countUniqueChars(s) = 5.
Given a string s, return the sum of countUniqueChars(t) where t is a substring of s.

Notice that some substrings can be repeated so in this case you have to count the repeated ones too.

Example 1:

Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A","B","C","AB","BC" and "ABC".
Every substring is composed with only unique letters.
Sum of lengths of all substring is 1 + 1 + 1 + 2 + 2 + 3 = 10
'''
class Solution:
    def uniqueLetterString(self, s: str) -> int:
        return self.solution2(s)

    # O(n) time | O(1) space, use moving sum
    def solution1(self, s: str) -> int:
        mp_prev = defaultdict(lambda: -1)
        mp_prevprev = defaultdict(lambda: -1)

        curr = 0
        res = 0

        for i, c in enumerate(s):
            curr += (i - mp_prev[c]) - (mp_prev[c] - mp_prevprev[c])
            mp_prevprev[c] = mp_prev[c]
            mp_prev[c] = i

            res += curr

        return res

    # O(n) time | O(1) space, use multiplication
    def solution2(self, s: str) -> int:
        mp_prev = defaultdict(lambda: -1)
        mp_prevprev = defaultdict(lambda: -1)

        curr = 0
        res = 0

        for i, c in enumerate(s):
            res += (i - mp_prev[c]) * (mp_prev[c] - mp_prevprev[c])
            mp_prevprev[c] = mp_prev[c]
            mp_prev[c] = i

        for k in range(26):
            c = chr(k + ord("A"))
            res += (len(s) - mp_prev[c]) * (mp_prev[c] - mp_prevprev[c])

        return res
