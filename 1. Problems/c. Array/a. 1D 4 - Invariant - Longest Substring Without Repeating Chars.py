# LC 3. Longest Substring Without Repeating Characters

'''
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    # O(N) time | O(1) space
    def optimized(self, s: str) -> int:
        mp = {}
        res = 0
        tail = -1

        for i in range(len(s)):
            if s[i] in mp:
                tail = max(mp[s[i]], tail)

            res = max(res, i - tail)
            mp[s[i]] = i

        return res

    # O(2N) time | O(1) space
    def lengthOfLongestSubstring(self, s: str) -> int:
        hmap = defaultdict(int)
        res = 0
        tail = -1

        for i in range(len(s)):
            hmap[s[i]] += 1

            while hmap[s[i]] > 1:
                tail += 1
                hmap[s[tail]] -= 1

            res = max(res, i - tail)

        return res
