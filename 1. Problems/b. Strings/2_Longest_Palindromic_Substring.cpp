// Longest Palindromic Substring

/*
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
*/

// my solution
class Solution {
public:
    int expand(string s, int left, int right){
        int L = left, R = right;
        while (L >= 0 && R < s.length() && s[L] == s[R]) {
            L--;
            R++;
        }
        return R - L - 1;
    }
    
    string longestPalindrome(string s) {
        int start = 0, end = 0;
        
        for (int i = 0; i < s.length(); i++) {
            int len1 = expand(s, i, i);
            int len2 = expand(s, i, i+1);
            cout << "length" << len1 << " " << len2 << endl;
            int len = max(len1, len2);
            
            if (len > end - start + 1) {
                start = i - (len - 1) / 2;
                end = i + len / 2;
                cout << start << " " << end << endl;
            }
        }
        
        return s.substr(start, end - start + 1);
    }
};