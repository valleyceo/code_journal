# LC 159. Longest Substring with At Most Two Distinct Characters

'''
Given a string s, return the length of the longest substring that contains at most two distinct characters.

Example 1:

Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.

Example 2:

Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.

Constraints:
1 <= s.length <= 105
s consists of English letters.
'''
# O(n) time | O(1) space
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        prev = None
        curr = None
        res = 0
        currCount = 0
        totalCount = 0

        for c in s:
            if c == curr:
                currCount += 1
                totalCount += 1
            elif c == prev:
                prev = curr
                curr = c
                totalCount += 1
                currCount = 1
            else:
                prev = curr
                curr = c

                res = max(res, totalCount)
                totalCount = currCount + 1
                currCount = 1

        return max(res, totalCount)
