// Reverse Integer

/*
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
*/

// my solution
#include <algorithm>
class Solution {
public:
    int reverse(int x) {
        
        bool n=false;
        
        if (x < 0) {
            n = true;
            x = -x;
        }
        
        int prev_x= 0, new_x=0;
        
        while (x != 0) {
            
            int d = x % 10;
            
            new_x = (new_x * 10) + d;
            
            // check overflow
            if ((new_x-d)/10 != prev_x) {
                return 0;
            }
            
            prev_x = new_x;
            x /= 10;
        }
        
        return n ? -new_x : new_x;
    }
};