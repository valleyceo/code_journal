// Contains Duplicate

/*
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
*/

// my solution
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.size() < 2)
            return false;
        
        sort(nums.begin(), nums.end());
        int temp = INT_MIN;
        for(int n : nums) {
            if (n == temp) {
                return true;
            }
            temp = n;
        }
        return false;
    }
    
};