"""
LC 84. Largest Rectangle in Histogram

/*
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

=> [0 0 5 5 0 0]

The largest rectangle is shown in the shaded area, which has area = 10 unit.

Example:

Input: [2,1,5,6,2,3]
Output: 10
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        
        for i in range(len(heights)):
            if len(stack) == 0 or heights[i] > heights[i-1]:
                stack.append(i)
            else:       
                while stack and heights[i] < heights[stack[-1]]:
                    h = heights[stack.pop()]
                    
                    if stack:
                        maxArea = max(maxArea, h*(i - stack[-1] - 1))
                    else:
                        maxArea = max(maxArea, h*i)
                        
                stack.append(i)
        
        while stack:
            h = heights[stack.pop()]
            
            if stack:
                maxArea = max(maxArea, h*(len(heights) - stack[-1] - 1))
            else:
                maxArea = max(maxArea, h*len(heights))
                
        return maxArea