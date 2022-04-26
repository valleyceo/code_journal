# LC 522. Longest Uncommon Subsequence II

'''
Given an array of strings strs, return the length of the longest uncommon subsequence between them. If the longest uncommon subsequence does not exist, return -1.

An uncommon subsequence between an array of strings is a string that is a subsequence of one string but not the others.

A subsequence of a string s is a string that can be obtained after deleting any number of characters from s.

For example, "abc" is a subsequence of "aebdc" because you can delete the underlined characters in "aebdc" to get "abc". Other subsequences of "aebdc" include "aebdc", "aeb", and "" (empty string).

Example 1:

Input: strs = ["aba","cdc","eae"]
Output: 3

Example 2:

Input: strs = ["aaa","aaa","aa"]
Output: -1
'''
# O(N^2) time | O(N) space
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def isSubset(w1, w2):
            idx = 0

            for c in w2:
                if idx < len(w1) and w1[idx] == c:
                    idx += 1

            return idx == len(w1)

        strs.sort(key = lambda x : -len(x))

        for i in range(len(strs)):
            hasSubset = False

            for j in range(len(strs)):
                if i == j:
                    continue

                if isSubset(strs[i], strs[j]):
                    hasSubset = True
                    break

            if not hasSubset:
                return len(strs[i])

        return -1
