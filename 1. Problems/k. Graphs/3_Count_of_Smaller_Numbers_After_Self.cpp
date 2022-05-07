// Count of Smaller Numbers After Self

/*
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Given nums = [5, 2, 6, 1]

To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Return the array [2, 1, 1, 0].
*/

// my solution
class Solution {
public:
    vector<int> countSmaller(vector<int>& nums) {
        if (nums.empty()) return {};
        
        vector<int>hash;
        vector<int>counts(nums.size());
        
        for (int i = nums.size() - 1; i >= 0; --i) {
            auto end = lower_bound(hash.begin(), hash.end(), nums[i]);
            counts[i] = end - hash.begin();
            hash.insert(end, nums[i]);
        }
        
        return counts;
    }
};