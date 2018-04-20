// Design Tic-Tac-Toe

/*
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
*/

// my solution - optimal
class TicTacToe {
public:
    
    /** Initialize your data structure here. */
    TicTacToe(int n): b_size(n), rows(n, 0), cols(n, 0), diag1(0), diag2(0) {}
    
    /** Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins. */
    int move(int row, int col, int player) {
        
        int p = (player == 1) ? 1 : -1;
        rows[row] += p;
        cols[col] += p;
        
        if (row == col)
            diag1 += p;
        
        if ((b_size-1-row) == col)
            diag2 += p;
        
        if (abs(diag1) == b_size || abs(diag2) == b_size || 
            abs(rows[row]) == b_size || abs(cols[col]) == b_size)
            return player;
        else
            return 0;
    }
    
private:
    vector<int> rows, cols;
    int diag1, diag2, b_size;
};

/**
 * Your TicTacToe object will be instantiated and called as such:
 * TicTacToe obj = new TicTacToe(n);
 * int param_1 = obj.move(row,col,player);
 */