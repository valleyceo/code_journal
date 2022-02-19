// Set Matrix Zeroes

/*
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
*/

// my solution - not in-place
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if (m == 0) return;
        
        int n = matrix[0].size();
        if (n == 0) return;
        
        vector<int> rows(m, 0);
        vector<int> cols(n, 0);
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (matrix[i][j] == 0) {
                    rows[i] += 1;
                    cols[j] += 1;
                }
            }
        }
        
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (rows[i]) {
                    matrix[i][j] = 0;
                } else if (cols[j]) {
                    matrix[i][j] = 0;
                }
                
            }
        }
        
        return;
    }
};