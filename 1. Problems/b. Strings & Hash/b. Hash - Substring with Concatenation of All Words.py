# 30. Substring with Concatenation of All Words

'''
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s) in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.

Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
Output: []

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
Output: [6,9,12]
'''
class Solution:
    # O((n - a*b) * a * b) time | O(a + b) space
    # n is length of string, a is length of words, b is length of each word
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        k = len(words)

        word_count = Counter(words)
        word_len = len(words[0])
        total_len = word_len * k

        def check(idx):
            rem_count = word_count.copy()
            words_used = 0

            for j in range(idx, idx + total_len, word_len):
                word = s[j : j + word_len]

                if rem_count[word] > 0:
                    rem_count[word] -= 1
                    words_used += 1
                else:
                    break

            return words_used == k

        res = []

        for i in range(n - total_len + 1):
            if check(i):
                res.append(i)

        return res
