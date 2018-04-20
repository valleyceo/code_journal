// Trapping Rain Water

/*
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
*/

// my solution
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.size() <= 1) 
            return 0;
        
        int res = 0;
        int left = 0;
        int right = height.size() - 1;
        
        int l_max = 0;
        int r_max = 0;
        
        while (left < right) {
            if (height[left] < height[right]) {
                height[left] >= l_max ? (l_max = height[left]) : (res += (l_max - height[left]));
                left++;
            } else {
                height[right] >= r_max ? (r_max = height[right]) : (res += (r_max - height[right]));
                right--;
            }
        }
        
        return res;
    }
};