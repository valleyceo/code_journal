// Largest Rectangle in Histogram

/*
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

=> [0 0 5 5 0 0]

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
*/


// my solution - optimal, space: O(n), time: O(n)
class Solution {
public:
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

// solution - Not optimal, Time: O(n^2), space: O(n)
//https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/29002/My-C++-DP-solution-16ms-easy-to-understand!
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        int ans = 0;
        int p;
        
        vector<int> left(n,0);
        vector<int> right(n,n);
        
        // process left
        for (int i = 1; i < n; ++i) {
            p = i - 1;
            
            while (p >= 0 && heights[i] <= heights[p])
                p = left[p] - 1;
            
            left[i] = p + 1;
        }
        
        // process right
        for (int i = n-2; i >= 0; --i) {
            p = i + 1;
            
            while (p < n && heights[i] <= heights[p])
                p = right[p];
            
            right[i] = p;
        }
        
        // get max area
        for (int i = 0; i < n; ++i)
            ans = max(ans, heights[i] * (right[i] - left[i]));
        
        return ans;
    }
};