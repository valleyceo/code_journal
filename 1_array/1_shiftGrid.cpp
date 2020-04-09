// Title

/*
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Example 1:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]

Example 2:

Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
*/

// my solution - O(N^2) time complexity, optimal
class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& grid, int k) {
        vector<int> arr;
        vector<vector<int>> res;
        
        for (auto r : grid) {
            arr.insert(arr.end(), r.begin(), r.end());
        }
        
        int m = k % arr.size();
        rotate(arr.begin(), arr.begin() + arr.size() - m, arr.end());
        
        for (int i = 0; i < grid.size(); ++i) {
            vector<int> temp;
            temp.insert(temp.begin(), arr.begin() + i*grid[0].size(), arr.begin() + (i+1)*grid[0].size());
            res.push_back(temp);
        }
        
        return res;
    }
};