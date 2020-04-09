// Contains Duplicate

/*
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
*/

// my solution - time: O(n + nlog(n)), space: O(1)
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

// better solution - time: O(n), space: O(n)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.size() < 2)
            return false;
        
        unordered_set<int> uset;
        
        for (int n : nums) {
            if (uset.find(n) != uset.end()) {
                return true;
            }
            uset.insert(n);
        }
        
        return false;
    }
};