# LC 424. Longest Repeating Character Replacement

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        return self.mySolution(s, k)

    # O(26*N) time | O(26) space
    def mySolution(self, s: str, k: int) -> int:
        def getMaxString(s, char):
            diff_char = 0
            tail_idx = 0
            res = 0

            for i in range(len(s)):
                if s[i] != char:
                    diff_char += 1

                    while diff_char > k:
                        if s[tail_idx] != char:
                            diff_char -= 1

                        tail_idx += 1

                res = max(res, i - tail_idx + 1)

            return res

        char_set = set(s)
        res = 0

        for c in char_set:
            res = max(res, getMaxString(s, c))

        return res

    # O(N) time | O(26)
    def onePassOptimal(self, s: str, k: int) -> int:
        max_repeat = 0
        count = defaultdict(int)
        res = 0

        for i in range(len(s)):
            count[s[i]] += 1
            max_repeat = max(max_repeat, count[s[i]])

            if res < max_repeat + k:
                res += 1
            else:
                count[s[i - res]] -= 1

        return res
