// Image Smoother

/*
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
*/

// my solution - time: O(N*M), space: O(N*M)
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        if (M.size() == 0 || M[0].size() == 0)
            return M;
        
        int rows = M.size();
        int cols = M[0].size();
        
        vector<vector<int>> res (rows, vector<int> (cols, 0));
        int rmin, rmax, cmin, cmax, ct;
        float tsum;
        
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                
                rmin = (i-1 >= 0) ? i - 1 : i;
                rmax = (i+1 < rows) ? i + 1 : i;
                cmin = (j-1 >= 0) ? j - 1 : j;
                cmax = (j+1 < cols) ? j + 1 : j;
                
                ct = (rmax - rmin + 1) * (cmax - cmin + 1);
                tsum = 0;
                
                for (int r = rmin; r <= rmax; r++)
                    for (int c = cmin; c <= cmax; c++)
                        tsum += M[r][c];
                        
                res[i][j] = int(tsum / float(ct));
            }
        }
        
        return res;
    }
};