// Excel Sheet Column Number

/*
Related to question Excel Sheet Column Title

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
*/

// my solution
class Solution {
public:
    int titleToNumber(string s) {
        int ans = 0;
        
        for (char a : s) {
            ans *= 26;
            ans += (a - 'A' + 1);
        }
        
        return ans;
    }
};