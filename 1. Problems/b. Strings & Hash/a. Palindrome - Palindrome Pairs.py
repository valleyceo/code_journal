# 336. Palindrome Pairs

'''
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.

Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]

Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wdict = {w: i for i, w in enumerate(words)}
        res = set()

        for i, word in enumerate(words):

            for j in range(len(word)+1):
                pre = word[:j]
                suf = word[j:]

                if pre == pre[::-1]:
                    if suf[::-1] in wdict and wdict[suf[::-1]] != i:
                        res.add((wdict[suf[::-1]], i))

                if suf == suf[::-1]:
                    if pre[::-1] in wdict and wdict[pre[::-1]] != i:
                        res.add((i, wdict[pre[::-1]]))

        return res
