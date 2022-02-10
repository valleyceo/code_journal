// Missing Ranges

/*
Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2", "4->49", "51->74", "76->99"].
*/

// my solution
class Solution {
public:
    string get_range(long long start, long long end) {
        return start==end ? to_string(start) : to_string(start) + "->" + to_string(end);
    }
    
    vector<string> findMissingRanges(vector<int>& nums, long long lower, long long upper) {
        vector<string> res;
        
        long long pre = lower - 1;
        
        for (int i = 0; i <= nums.size(); i++) {
            long long cur = (i == nums.size() ? upper + 1 : nums[i]);
            
            if (cur-pre >= 2)
                res.push_back(get_range(pre+1, cur-1));
                pre = cur;
        }
        
        return res;
    }
};