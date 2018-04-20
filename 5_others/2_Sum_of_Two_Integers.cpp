// Sum of Two Integers

/*
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
*/

// my solution
class Solution {
public:
    int getSum(int a, int b) {
        int ans = a ^ b;
        int c = a & b;
        
        while (c != 0) {
            c <<= 1;
            int ans_next = ans ^ c;
            c = ans & c;
            ans = ans_next;
        }
        
        return ans;
    }
};