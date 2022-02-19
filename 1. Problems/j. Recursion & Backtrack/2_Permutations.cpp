// Permutations


/*
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
*/

// my solution
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> result;
        
        permuteRecursive(nums, 0, result);
        return result;
    }
    
    void permuteRecursive(vector<int> &nums, int begin, vector<vector<int>> &result) {
        
        if (begin >= nums.size()) {
            result.push_back(nums);
            return;
        }
        
        for (int i = begin; i < nums.size(); i++) {
            swap(nums[begin], nums[i]);
            permuteRecursive(nums, begin + 1, result);
            //reset
            swap(nums[begin], nums[i]);
        }
        
    }
};