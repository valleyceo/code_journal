// Find All Numbers Disappeared in an Array

/*
Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
*/

// my solution - time: O(n), space: O(1), optimal
class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        vector<int> res;
        
        for (auto a : nums)
            if (nums[abs(a)-1] < 0)
                continue;
            else
                nums[abs(a)-1] *= -1;
        
        for (int i = 0; i < nums.size(); i++)
            if (nums[i] > 0)
                res.push_back(i+1);
        
        return res;
    }
};