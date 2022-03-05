# 127. Word Ladder

'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''
# O(N*M^2) time | O(N * M^2) space
# N is number of words and M is length of each word
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        masks = defaultdict(list)

        for word in wordList:
            for i, char in enumerate(word):
                masks[word[:i] + '*' + word[i+1:]].append(word)

        steps = 1
        que = [beginWord]

        while que:
            temp = []

            while que:
                curr_word = que.pop()

                if curr_word == endWord:
                    return steps

                for i, char in enumerate(curr_word):
                    mask = curr_word[:i] + '*' + curr_word[i+1:]

                    if mask in masks:
                        temp.extend(masks[mask])
                        del masks[mask]

            steps += 1
            que = temp

        return 0
