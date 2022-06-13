# LC 2131. Longest Palindrome by Concatenating Two Letter Words

'''
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created.
'''
# O(n) time | O(26 * 26) space
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        wcount = defaultdict(int)
        odd_count = 0
        res = 0

        for word in words:
            if word[0] == word[1]:
                if wcount[word] > 0:
                    wcount[word] -= 1
                    odd_count -= 1
                    res += 4
                else:
                    wcount[word] += 1
                    odd_count += 1
            else:
                rword = word[::-1]

                if wcount[rword] > 0:
                    wcount[rword] -= 1
                    res += 4
                else:
                    wcount[word] += 1

        if odd_count > 0:
            res += 2

        return res
