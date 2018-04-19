// Valid Sudoku

/*
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

*/

// my solution - 25ms, 37% -> optimal computational complexity
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        // check horizontals
        for (int i = 0; i < board.size(); i++) {
            
            vector<bool> check_box(10, false);
            
            for (int j = 0; j < board.size(); j++) {
                if (board[i][j] == '.')
                    continue;
                
                if (check_box[board[i][j]]) {
                    return false;
                } else {
                    check_box[board[i][j]] = true;
                }
            }
        }
                              
        // check verticals
        for (int i = 0; i < board.size(); i++) {
            
            vector<bool> check_box(10, false);
            
            for (int j = 0; j < board.size(); j++) {
                if (board[j][i] == '.')
                    continue;
                
                if (check_box[board[j][i]]) {
                    return false;
                } else {
                    check_box[board[j][i]] = true;
                }
            }
        }
        
        // check sub-boxes
        for (int i = 0; i < board.size(); i+=3) {
            for (int j = 0; j < board.size(); j+=3) {
                
                vector<bool> check_box(10, false);
                
                for (int a = i; a < i+3; a++) {
                    for (int b = j; b < j+3; b++) {
                        if (board[a][b] == '.')
                            continue;
                        
                        if (check_box[board[a][b]]) {
                            return false;
                        } else {
                            check_box[board[a][b]] = true;
                        }
                    }
                }
            }
        }
        
        return true;
    }
};