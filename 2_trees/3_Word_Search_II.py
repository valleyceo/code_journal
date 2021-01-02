"""
LC 212 Word Search II

Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example 1:

Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:

Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
"""
# Trie solution
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