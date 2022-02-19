// Factorial Trailing Zeroes

/*
Given an integer n, return the number of trailing zeroes in n!.

Note: Your solution should be in logarithmic time complexity.
*/

// my solution
class Solution {
public:
    int trailingZeroes(int n) {
        
    int result = 0;
    
    for(long long i=5; n/i>0; i*=5){
        result += (n/i);
    }
        
    return result;
    }
};