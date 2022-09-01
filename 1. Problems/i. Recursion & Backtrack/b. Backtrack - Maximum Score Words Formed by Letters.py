# 1255. Maximum Score Words Formed by Letters

'''
Given a list of words, list of  single letters (might be repeating) and score of every character.

Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).

It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

Example 1:

Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
Output: 23
Explanation:
Score  a=1, c=9, d=5, g=3, o=2
Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
Words "dad" and "dog" only get a score of 21.
'''

class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        res = 0

        def backtrack(i, curr_score, letters_left):
            nonlocal res

            if i == len(words):
                res = max(res, curr_score)
                return

            temp = letters_left.copy()
            point = search(words[i], temp)

            if point != -1:
                backtrack(i + 1, point + curr_score, temp)

            backtrack(i + 1, curr_score, letters_left)
            return

        def search(word, letters_rem):
            point = 0

            for c in word:
                if letters_rem[c] > 0:
                    letters_rem[c] -= 1
                    point += score[ord(c) - ord('a')]
                else:
                    return -1

            return point

        letters_count = Counter(letters)
        backtrack(0, 0, letters_count)

        return res
