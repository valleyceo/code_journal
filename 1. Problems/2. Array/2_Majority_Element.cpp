// Majority Element

/*
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.
*/

// my solution
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        // Moore voding algorithm
        int c = 0, majority;
        
        for (int n : nums){
            if (c == 0) {
                majority = n;
            }
            
            if (majority == n) {
                c++;
            } else {
                c--;
            }
        }
        return majority;
    }
};