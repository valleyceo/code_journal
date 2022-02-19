#include <iostream>
#include <vector>

using namespace std;
int rows, cols;

void search(int r, int c, vector<vector<int>> map, vector<vector<bool>>& visited) {
  if (visited[r][c])
    return;
  
  if (!map[r][c]) {
    visited[r][c] = true;
    return;
  }
    
  visited[r][c] = true;
  // search
  if (r-1 >= 0) search(r-1, c, map, visited);
  if (r+1 < rows) search(r+1, c, map, visited);
  if (c-1 >= 0) search(r, c-1, map, visited);
  if (c+1 < cols) search(r, c+1, map, visited); 
  
  return;
}
int getNumberOfIslands( const vector<vector<int>>& binaryMatrix ) 
{
  // your code goes here
  rows = binaryMatrix.size();
  cols = binaryMatrix[0].size();
  
  vector<vector<bool>> visited(rows, vector<bool>(cols, false));
  
  int count = 0;
  for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
      if (binaryMatrix[i][j] == 1 && !visited[i][j]) {
        search(i, j, binaryMatrix, visited);
        count++;
      }
    }
  }
  
  return count;
}

int main() {
  vector<vector<int>> x = {{1, 0, 1, 0}};
  cout << getNumberOfIslands(x) << endl;
  return 0;
}

/*
Notes:
- given 2D matrix
- count number of islands (1)
- adjacent if they are next to each other (row, col)
- diagonal neighbors are not adjacent

Input:
- 2D matrix

Output:
- Int (max < 100)

Limits:
- time: 5000ms
- row, col: 1~100

Time complexity: O(row*col)
Space complexity: O(row*col)
*/