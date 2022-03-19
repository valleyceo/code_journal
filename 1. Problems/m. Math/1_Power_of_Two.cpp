// Power of Two

/*
Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Example 2:

Input: 16
Output: true
Example 3:

Input: 218
Output: false
*/

// my solution
class Solution {
public:
    bool isPowerOfTwo(int n) {
        if (n <= 0)
            return false;
        
        return (n & (n-1)) == 0;
    }
    
    /*
    bool isPowerOfTwo(int n) {
        if (n <= 0)
            return false;
        
        int ct = 0;
        while (n) {
            ct += n & 1;
            n >>= 1;
        }
        
        return ct == 1 ? true : false;
    }
    */
};