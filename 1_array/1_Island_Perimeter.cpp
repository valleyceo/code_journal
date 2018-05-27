// Island Perimeter

/*
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
    -
  0|1|0,0
  -   -
 |1,1,1|0
  -   -
  0|1|0,0
  -
 |1,1|0,0
  - -
*/

// my solution
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0)
            return 0;
        
        int ct = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == 1) {
                    if (i == 0 || grid[i-1][j] == 0) ct++;
                    if (j == 0 || grid[i][j-1] == 0) ct++;
                    if (i == grid.size()-1 || grid[i+1][j] == 0) ct++;
                    if (j == grid[0].size()-1 || grid[i][j+1] == 0) ct++;
                }
            }
        }
        
        return ct;
    }
};

// Alternate (if there are more 1s this could be faster)
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        if (grid.size() == 0 || grid[0].size() == 0)
            return 0;
        
        int ct = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                // edges
                if (i == 0 && grid[i][j] == 1) ct++;
                if (j == 0 && grid[i][j] == 1) ct++;
                if (i == grid.size()-1 && grid[i][j] == 1) ct++;
                if (j == grid[0].size()-1 && grid[i][j] == 1) ct++;
                
                // non edges
                if (i != 0 && grid[i][j] != grid[i-1][j]) ct++;
                if (j != 0 && grid[i][j] != grid[i][j-1]) ct++;
            }
        }
        
        return ct;
    }
};