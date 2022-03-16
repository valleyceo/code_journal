# 84. Largest Rectangle in Histogram

'''
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:

Input: heights = [2,4]
Output: 4
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.monostack(heights)

    # O(n) time | O(n) space
    def monostack(self, heights: List[int]) -> int:
        stack = [-1]
        res = 0

        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                curr_height = heights[stack.pop()]
                curr_width = i - stack[-1] - 1
                res = max(res, curr_height * curr_width)

            stack.append(i)

        while stack[-1] != -1:
            curr_height = heights[stack.pop()]
            curr_width = len(heights) - stack[-1] - 1
            res = max(res, curr_height * curr_width)

        return res


    # TLE solution, O(nlogn) avg, O(n^2) worst time | O(n) space
    def divideConquer(self, heights: List[int]) -> int:
        def recurse(left, right) -> int:
            if left > right:
                return 0

            minIdx = left

            for i in range(left, right + 1):
                if heights[i] < heights[minIdx]:
                    minIdx = i

            return max([heights[minIdx] * (right - left + 1),
                        recurse(left, minIdx - 1), recurse(minIdx + 1, right)])

        return recurse(0, len(heights) - 1)
