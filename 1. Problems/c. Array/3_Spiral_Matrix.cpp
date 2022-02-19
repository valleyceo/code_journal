// Spiral Matrix

/*
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
*/

// my solution - optimal
class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        
        if (matrix.size() == 0 || matrix[0].size() == 0)
            return res;
        
        int m = matrix.size();
        int n = matrix[0].size();
        
        vector<int> spiral(m * n);
        
        int u = 0, d = m - 1, l = 0, r = n - 1, k = 0;
        
        while(true) {
            // upper left->right
            for (int col = l; col <= r; col++)
                spiral[k++] = matrix[u][col];
            
            if (++u > d) break;
            
            // right side top->down
            for (int row = u; row <= d; row++)
                spiral[k++] = matrix[row][r];
            
            if (--r < l) break;
            
            // lower right->left
            for (int col = r; col >= l; col--)
                spiral[k++] = matrix[d][col];
            
            if (--d < u) break;
            
            // left side down->top
            for (int row = d; row >= u; row--)
                spiral[k++] = matrix[row][l];
            
            if (++l > r) break;
        }
        
        return spiral;
    }
};