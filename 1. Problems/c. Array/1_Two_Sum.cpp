// Two Sum

/*
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

// my solution
class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        map<int, int> map;
        
        for (int i = 0; i < numbers.size(); i++)
            if (map.find(target-numbers[i]) != map.end())
                return vector<int>{map[target-numbers[i]]+1, i+1};
            else
                map[numbers[i]] = i;
            
        return vector<int>{};
    }
};