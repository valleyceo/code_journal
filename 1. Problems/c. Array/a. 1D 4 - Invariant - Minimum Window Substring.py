# 76. Minimum Window Substring

'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''
# O(M + N) time | O(N) space, where N is t (lookup string)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        maxLeft = 0
        maxRight = 0
        left = 0
        counter = Counter(t)
        missing = len(t)

        for right, char in enumerate(s, 1):

            if counter[char] > 0:
                missing -= 1

            counter[char] -= 1

            if missing == 0:
                while left < right and counter[s[left]] < 0:
                    counter[s[left]] += 1
                    left += 1

                if maxRight == 0 or right - left < maxRight - maxLeft:
                    maxLeft = left
                    maxRight = right

                missing += 1
                counter[s[left]] += 1
                left += 1

        return s[maxLeft:maxRight]
