// Single Number II

/*
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

Note:
[1 1 1 2]

Init:
a = 000
b = 000
1st loop (1):
a = a ^ (1 & ~b) = 000 ^ (001 & 111) = 000 ^ 001 = 001
b = b ^ (001 & 110) = 000 ^ 000 = 000

2nd loop (1):
a = 001 ^ (001 & 111) = 000
b = 000 ^ (001 & 111) = 000 ^ 001 = 001

3rd loop (1):
a = 000 ^ (001 & 110) = 000 ^ 000 = 000
b = 001 ^ (001 & 111) = 001 ^ 001 = 000
*/

// my solution
class Solution {
public:
    /*
    int singleNumber(vector<int>& nums) {
        
        unordered_map<int, int> umap;
        
        for (auto a : nums) {
            if (umap[a] == 2)
                umap[a] = 0;
            else
                umap[a]++;
        }
        
        for (auto a : umap) {
            if (a.second == 1)
                return a.first;
        }
        
        return -1;
    }
    */
    int singleNumber(vector<int>& nums) {
        int a = 0;
        int b = 0;

        for (auto n : nums)
        {
            a ^= n & ~b;
            b ^= n & ~a;
        }
        
        return a;
    }
};