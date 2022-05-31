# LC 792. Number of Matching Subsequences

'''
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".

Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
'''
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        return self.pointerMap(s, words)

    # O(M * N) time | O(M + N) space
    def mySolution(self, s: str, words: List[str]) -> int:
        def isSubsequence(pattern, sub_pattern):
            idx = 0
            for c, count in pattern:
                if c == sub_pattern[idx][0]:
                    use = min(count, sub_pattern[idx][1])
                    sub_pattern[idx][1] -= use

                    if sub_pattern[idx][1] == 0:
                        idx += 1

                if idx == len(sub_pattern):
                    return True

            return False

        def getPattern(word):
            p = []
            prev = ""
            count = 0

            for c in word:
                if c != prev:
                    if prev != "":
                        p.append([prev, count])
                    prev = c
                    count = 1
                else:
                    count += 1

            if count > 0:
                p.append([prev, count])

            return p

        res = 0
        pattern = getPattern(s)

        for word in words:
            if isSubsequence(pattern, getPattern(word)):
                res += 1

        return res

    # O(len(s) + sum(len(words[i])) time | O(len(words))
    def pointerMap(self, s: str, words: List[str]) -> int:
        res = 0
        word_map = [[] for _ in range(26)]

        for w in words:
            word_map[ord(w[0]) - ord('a')].append(w)

        for c in s:
            match_words = word_map[ord(c) - ord('a')]
            word_map[ord(c) - ord('a')] = []

            for mw in match_words:
                if len(mw) == 1:
                    res += 1
                    continue

                word_map[ord(mw[1]) - ord('a')].append(mw[1:])

        return res
