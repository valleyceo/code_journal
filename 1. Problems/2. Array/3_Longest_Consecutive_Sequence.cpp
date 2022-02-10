// Longest Consecutive Sequence

/*
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
*/

// my solution - optimal
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (nums.size() == 0)
            return 0;
        
        unordered_set<int> umap(nums.begin(), nums.end());
        int res = 1;
        
        for (int n : nums) {
            if (umap.find(n) == umap.end()) continue;
            
            umap.erase(n);
            int prev = n-1, next = n+1;
            
            while (umap.find(prev) != umap.end())
                umap.erase(prev--);
            
            while (umap.find(next) != umap.end())
                umap.erase(next++);
            
            res = max(res, next-prev-1);
        }
        
        return res;
    }
};