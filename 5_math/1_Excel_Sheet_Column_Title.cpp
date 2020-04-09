// Excel Sheet Column Title

/*
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
*/

// my solution - optimal
class Solution {
public:
    string convertToTitle(int n) {
        string res = "";
        
        if (n <= 0) return "";
        
        while (n) {
            res += (--n % 26 + 'A');
            n = n / 26;
        }
        
        reverse(res.begin(), res.end());
        
        return res;
    }
};

/*
Trick
- Need to subtract by 1 because A-Z should be indexed from 0 (from 1-26 to 0-25) such that dividing 26 does not count the modulus (ex. Z: 26/26 = 1)

*/