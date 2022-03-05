# 425. Word Squares

'''
Given an array of unique strings words, return all the word squares you can build from words. The same word from words can be used multiple times. You can return the answer in any order.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

Example 1:

Input: words = ["area","lead","wall","lady","ball"]
Output: [["ball","area","lead","lady"],["wall","area","lead","lady"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Example 2:

Input: words = ["abat","baba","atan","atal"]
Output: [["baba","abat","baba","atal"],["baba","abat","baba","atan"]]
Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).

Constraints:
1 <= words.length <= 1000
1 <= words[i].length <= 4
All words[i] have the same length.
words[i] consists of only lowercase English letters.
All words[i] are unique.
'''
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        wdict = defaultdict(list)

        for word in words:
            for i in range(len(word) + 1):
                wdict[word[:i]].append(word)

        wlist = [""] * len(words[0])
        self.res = []
        self.backtrack([], wlist, wdict, words)

        return self.res

    def backtrack(self, wordPath, wlist, wdict, words):
        if len(wordPath) == len(words[0]):
            self.res.append(wordPath)
            return

        idx = len(wordPath)
        for word in wdict[wlist[idx]]:
            temp = []
            isValid = True

            for lw, ww in zip(wlist, list(word)):
                if lw + ww in wdict:
                    temp.append(lw + ww)
                else:
                    isValid = False
                    break

            if not isValid:
                continue

            self.backtrack(wordPath + [word], temp, wdict, words)
