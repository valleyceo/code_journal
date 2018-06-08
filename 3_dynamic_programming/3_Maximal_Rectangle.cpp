// Maximal Rectangle

/*
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
*/

// my solution
class Solution {
public:
    int maximalRectangle(vector<vector<char>>& matrix) {
        if (matrix.size() == 0 || matrix[0].size() == 0) return 0;
        
        vector<int> dp ( matrix[0].size(), 0 );
        int max_area = 0;
        for (int i = 0; i < matrix.size(); i++) {
            for (int j = 0; j < matrix[0].size(); j++) {
                if (matrix[i][j] == '1')
                    dp[j]++;
                else
                    dp[j] = 0;
            }
            
            max_area = max(max_area, largestRectangleArea(dp));
        }
        
        return max_area;
    }
    
private:
    int largestRectangleArea(vector<int> &height) {
        stack<int> stk;
        int idx, max_area = 0, area = 0;

        for (idx = 0; idx < height.size();) {
            if (stk.empty() || height[stk.top()] <= height[idx]) {
                stk.push(idx++);
            } else {
                int top = stk.top();
                stk.pop();

                if (stk.empty()) {
                    area = height[top] * idx;
                } else {
                    area = height[top] * (idx - stk.top() - 1);
                }

                max_area = max(max_area, area);
            }
        }

        while (!stk.empty()) {
            int top = stk.top();
            stk.pop();
            
            if (stk.empty()) {
                area = height[top] * idx;
            } else {
                area = height[top] * (idx - stk.top() - 1);
            }

            max_area = max(max_area, area);
        }

        return max_area;
    }
};