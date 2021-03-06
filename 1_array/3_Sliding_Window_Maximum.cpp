// Sliding Window Maximum

/*
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?
*/

// my solution
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> res;
        
        if (n == 0) return res;
        
        deque<int> max;
        
        for (int i = 0; i < n; i++) {
            while (!max.empty() && nums[i] > max.back()) {
                max.pop_back();
            }
            
            max.push_back(nums[i]);
            
            if (i >= k - 1) {
                res.push_back(max.front());
                
                if (nums[i - k + 1] == max.front())
                    max.pop_front();
            }
        }
        return res;
    }
};