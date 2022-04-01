# LC 320. Generalized Abbreviation

'''
A word's generalized abbreviation can be constructed by taking any number of non-overlapping and non-adjacent substrings and replacing them with their respective lengths.

For example, "abcde" can be abbreviated into:
"a3e" ("bcd" turned into "3")
"1bcd1" ("a" and "e" both turned into "1")
"5" ("abcde" turned into "5")
"abcde" (no substrings replaced)
However, these abbreviations are invalid:
"23" ("ab" turned into "2" and "cde" turned into "3") is invalid as the substrings chosen are adjacent.
"22de" ("ab" turned into "2" and "bc" turned into "2") is invalid as the substring chosen overlap.
Given a string word, return a list of all the possible generalized abbreviations of word. Return the answer in any order.

Example 1:

Input: word = "word"
Output: ["4","3d","2r1","2rd","1o2","1o1d","1or1","1ord","w3","w2d","w1r1","w1rd","wo2","wo1d","wor1","word"]

Example 2:

Input: word = "a"
Output: ["1","a"]
'''

class Solution:
    # O(n * 2^n) time | O(2^n) space (O(n) using append/pop)
    def generateAbbreviations(self, word: str) -> List[str]:
        def backtrack(idx, count, path):
            if len(word) == idx:
                ct_str = str(count) if count > 0 else ""
                res.append(path + ct_str)
                return

            backtrack(idx + 1, count + 1, path)
            ct_str = str(count) if count > 0 else ""
            backtrack(idx + 1, 0, path + ct_str + word[idx])

        res = []
        backtrack(0, 0, "")
        return res

    # O(n * 2^n) time | O(n) space
    def bitmask(self, word: str) -> List[str]:
        def bitWord(bit):
            new_word = ""
            count = 0
            for i, b in enumerate(bit):
                if b == "0":
                    new_word += str(count) if count > 0 else ""
                    new_word += word[i]
                    count = 0
                else:
                    count += 1

            new_word += str(count) if count > 0 else ""
            return new_word

        res = []
        mask = 2**(len(word))

        for i in range(2**len(word)):
            bit = mask | i
            new_word = bitWord(bin(bit)[3:])
            res.append(new_word)

        return res
