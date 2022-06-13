# LC 2135. Count Words Obtained After Adding a Letter

'''
You are given two 0-indexed arrays of strings startWords and targetWords. Each string consists of lowercase English letters only.

For each string in targetWords, check if it is possible to choose a string from startWords and perform a conversion operation on it to be equal to that from targetWords.

The conversion operation is described in the following two steps:

Append any lowercase letter that is not present in the string to its end.
For example, if the string is "abc", the letters 'd', 'e', or 'y' can be added to it, but not 'a'. If 'd' is added, the resulting string will be "abcd".
Rearrange the letters of the new string in any arbitrary order.
For example, "abcd" can be rearranged to "acbd", "bacd", "cbda", and so on. Note that it can also be rearranged to "abcd" itself.
Return the number of strings in targetWords that can be obtained by performing the operations on any string of startWords.

Note that you will only be verifying if the string in targetWords can be obtained from a string in startWords by performing the operations. The strings in startWords do not actually change during this process.

Example 1:

Input: startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]
Output: 2
'''
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        return self.bitMaskSolution(startWords, targetWords)

    def mySolution(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = set()

        for word in startWords:
            start_set.add("".join(sorted(word)))

        res = 0

        for word in targetWords:

            sorted_word = "".join(sorted(word))

            for i in range(len(sorted_word)):
                if sorted_word[:i] + sorted_word[i+1:] in start_set:
                    res += 1
                    break

        return res

    def bitMaskSolution(self, startWords: List[str], targetWords: List[str]) -> int:
        start_set = set()
        res = 0

        for word in startWords:
            mask = 0

            for c in word:
                mask ^= 1 << ord(c) - ord('a')

            start_set.add(mask)

        for word in targetWords:
            mask = 0

            for c in word:
                mask ^= 1 << ord(c) - ord('a')

            for c in word:
                if mask ^ (1 << ord(c) - ord('a')) in start_set:
                    res += 1
                    break

        return res
