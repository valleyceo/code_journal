# LC 245. Shortest Word Distance III

'''
Given an array of strings wordsDict and two strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Note that word1 and word2 may be the same. It is guaranteed that they represent two individual words in the list.

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "makes"
Output: 3
'''
class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        return self.cleanSolution(wordsDict, word1, word2)

    def cleanSolution(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        idx1 = -1
        idx2 = -1

        for i, word in enumerate(wordsDict):
            if word == word1:
                idx1 = i

                if idx2 != -1:
                    res = min(res, idx1 - idx2)

            if word == word2:
                idx2 = i

                if idx1 != -1 and idx1 != idx2:
                    res = min(res, idx2 - idx1)

        return res

    def naiveSolution(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pos_map = defaultdict(list)

        for i, word in enumerate(wordsDict):
            pos_map[word].append(i)


        arr1 = pos_map[word1]
        arr2 = pos_map[word2]
        res = float('inf')

        if word1 == word2:
            for i in range(1, len(arr1)):
                res = min(res, arr1[i] - arr1[i-1])
        else:
            idx1 = 0
            idx2 = 0
            while idx1 < len(arr1) and idx2 < len(arr2):
                diff = abs(arr1[idx1] - arr2[idx2])
                res = min(res, diff)

                if idx1 == len(arr1) - 1:
                    idx2 += 1
                    continue
                elif idx2 == len(arr2) - 1:
                    idx1 += 1
                    continue

                if arr1[idx1] <= arr2[idx2]:
                    idx1 += 1
                else:
                    idx2 += 1

        return res
