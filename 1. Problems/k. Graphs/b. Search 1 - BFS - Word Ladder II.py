# 126. Word Ladder II

'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return all the shortest transformation sequences from beginWord to endWord, or an empty list if no such sequence exists. Each sequence should be returned as a list of the words [beginWord, s1, s2, ..., sk].

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
Explanation: There are 2 shortest transformation sequences:
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        graph = defaultdict(list)
        res = []

        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + "*" + word[i+1:]].append(word)

        queue = deque([[beginWord]])
        visited = set()

        while queue:
            path = queue.popleft()
            curr_word = path[-1]
            visited.add(curr_word)

            if curr_word == endWord:
                if len(res) == 0 or len(res[-1]) > len(path):
                    res = [path[:]]
                elif len(res[-1]) == len(path):
                    res.append(path[:])

                continue

            for i in range(len(curr_word)):
                mask = curr_word[:i] + '*' + curr_word[i+1:]

                for next_word in graph[mask]:
                    if next_word == curr_word or next_word in path:
                        continue

                    if next_word in visited:
                        continue

                    queue.append(path + [next_word])

        return res
