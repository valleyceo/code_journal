// Rotate Image

/*
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
*/

// my solution
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        if (matrix.size() < 2) {
            return;
        }
        
        int m = matrix.size();
        int m1 = m/2;
        int m2 = m/2;
        int temp;
        
        if (m % 2 == 1) {
            m2 += 1;
        }
        
        for (int i = 0; i < m1; i++) {
            for (int j = 0; j < m2; j++) {
                
                temp = matrix[i][j];
                matrix[i][j] = matrix[m-j-1][i];
                matrix[m-j-1][i] = matrix[m-i-1][m-j-1];
                matrix[m-i-1][m-j-1] = matrix[j][m-i-1];
                matrix[j][m-i-1] = temp;
            }
        }
        
        return;
    }
};