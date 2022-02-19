// 4Sum

/*
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.
*/

// optimal - n^2log(n)
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res{}; 
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < nums.size(); ++i) {
            for (int j = i+1; j < nums.size(); ++j) {
                int l = j + 1;
                int r = nums.size()-1;
                
                while (l < r) {
                    int sum = nums[i] + nums[j] + nums[l] + nums[r];
                    
                    if (sum == target) {
                        vector<int> tmp{ nums[i], nums[j], nums[l], nums[r] };
                        
                        if (res.end() == find(res.begin(), res.end(), tmp)) {
                            res.push_back( { nums[i], nums[j], nums[l], nums[r] } );
                        }
                        l++; r--;
                    } else if (sum < target) {
                        l++;
                    } else {
                        r--;
                    }
                }
            }
        }
        
        return res;
    }
};