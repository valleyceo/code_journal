// Game of Life

/*
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state.

Follow up: 
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
*/

// my solution
class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        int m = board.size();
        if (m == 0) return;
        int n = board[0].size();
        
        for(int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int count = 0;
                
                for(int p = max(0, i-1); p < min(m, i+2); ++p) {
                    for (int q = max(0, j-1); q < min(n, j+2); ++q) {
                        if (board[p][q] & 1) {
                            ++count;
                        }
                    }
                }
                
                if (count == 3 || count - board[i][j] == 3) {
                    board[i][j] = board[i][j] | 2;
                }
            }
        }
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                board[i][j] = board[i][j] >> 1;
            }
        }
    }
};