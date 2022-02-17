// Word Search

/*
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
*/

// my solution
class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        rows = static_cast<int>(board.size());
        cols = static_cast<int>(board[0].size());
        
        for (int i=0; i<rows; i++) {
            for (int j=0; j<cols; j++) {
                if (exist(board, word, i, j, 0)) {
                    return true;
                }
            }
        }
        
        return false;
    }
    
private:
    int rows, cols;
    bool exist(vector<vector<char>>& board, string& word, int row, int col, int pos) {
        if (board[row][col] != word[pos] || board[row][col] == ' ')
            return false;
        else if (pos == word.size() - 1)
            return true;
        
        char c = board[row][col];
        board[row][col] = ' ';
        
        if (row > 0 && exist(board, word, row - 1, col, pos + 1) ||
            row < rows - 1 && exist(board, word, row + 1, col, pos + 1) ||
            col > 0 && exist(board, word, row, col - 1, pos + 1) ||
            col < cols - 1 && exist(board, word, row, col + 1, pos + 1)) {
            board[row][col] = c;
            return true;
        }
        
        board[row][col] = c;
        return false;
    }
};