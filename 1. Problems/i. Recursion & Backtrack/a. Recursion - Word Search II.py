# LC 212. Word Search II

'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
Return ["eat","oath"].
Note:
You may assume that all inputs are consist of lowercase letters a-z.

click to show hint.

You would need to optimize your backtracking to pass the larger test. Could you stop backtracking earlier?

If the current candidate does not exist in all words' prefix, you could stop backtracking immediately. What kind of data structure could answer such query efficiently? Does a hash table work? Why or why not? How about a Trie? If you would like to learn how to implement a basic trie, please work on this problem: Implement Trie (Prefix Tree) first.
'''

class Solution:
    class TrieNode:
        def __init__(self):
            self.isWord = False
            self.next = {}

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.root = self.TrieNode()

        for word in words:
            node = self.root

            for char in word:
                if char not in node.next:
                    node.next[char] = self.TrieNode()

                node = node.next[char]

            node.isWord = True

        self.res = set()
        self.dir = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for i in range(len(board)):
            for j in range(len(board[0])):
                startNode = self.root
                self.searchWord(i, j, startNode, "", set(), board)

        return list(self.res)

    def searchWord(self, r: int, c: int, node: TreeNode, word: str, path: set, board: List[List[str]]):

        if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
            return

        if board[r][c] not in node.next:
            return

        if (r, c) in path:
            return

        path.add((r, c))
        node = node.next[board[r][c]]

        if node.isWord:
            self.res.add(word + board[r][c])

        for dr, dc in self.dir:

            self.searchWord(r + dr, c + dc, node, word + board[r][c], path, board)

        path.remove((r, c))
