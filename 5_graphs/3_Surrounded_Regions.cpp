// Surrounded Regions

/*
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

For example,
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
*/

// my solution
class Solution {
public:
    void check(vector<vector<char>>& board, int r, int c) {
        if (board[r][c] != 'O')
            return;
        
        board[r][c] = '1';
        if (c-1 >= 0)
            check(board, r, c-1);
        if (r-1 >= 0)
            check(board, r-1, c);
        if (c+1 < board[0].size())
            check(board, r, c+1);
        if (r+1 < board.size())
            check(board, r+1, c);
        
        return;
    }
    
    void solve(vector<vector<char>>& board) {
        if (board.size() == 0 || board[0].size() == 0) {
            return;
        }
        
        int m = board.size();
        int n = board[0].size();
        
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O')
                check(board, i, 0);
            
            if (board[i][n-1] == 'O')
                check(board, i, n-1);
        }
        
        for (int i = 0; i < n; i++) {
            if (board[0][i] == 'O')
                check(board, 0, i);
            
            if (board[m-1][i] == 'O') {
                check(board, m-1, i);
            }
                
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
            }
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == '1')
                    board[i][j] = 'O';
            }
        }
        
        return;
    }
};