// Decode Ways

/*
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
*/

// my solution
class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        
        if (n == 0)
            return 0;
        
        int n0 = 1;
        int n1 = (s[0] == '0') ? 0 : 1;
        
        for (int i = 1; i < n; i++) {
            int temp = n1;
            
            if (s[i] == '0')
                n1 = 0;
            
            if ((s[i-1] == '2' && s[i] <= '6') || s[i-1] == '1')
                n1 += n0;
            
            if (n1 == 0) 
                return 0;
            
            n0 = temp;
        }
        
        return n1;
    }
};