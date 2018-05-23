// Add Binary

/*
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
*/

// my solution
class Solution {
public:
    string addBinary(string a, string b) {
        int al = a.length()-1;
        int bl = b.length()-1;
        int val = 0, carry = 0;
        string res = "";
        
        while (al >=0 || bl >= 0) {
            val = carry;
            carry = 0;
            
            if (al >=0 && a[al] == '1') {
                val += 1;
            }
            
            if (bl >=0 && b[bl] == '1') {
                val += 1;
            }
            
            if (val > 1) {
                carry = 1;
                val -= 2;
            }
            
            if (val == 1)
                res.insert(0, "1");
            else
                res.insert(0, "0");
            
            bl--;
            al--;
        }
        
        if (carry) {
            res.insert(0, "1");
        }
        
        return res;
    }
};