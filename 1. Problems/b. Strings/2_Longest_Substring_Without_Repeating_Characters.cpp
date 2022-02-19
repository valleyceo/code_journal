// Longest Substring Without Repeating Characters

/*
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/

// my solution
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        string ss = "";
        int max_str = 0;
        bool isnew;
        
        for (char a : s) {
            
            isnew = true; 
            
            for (int i=0; i<ss.length(); i++) {
                if (a == ss[i]) {
                    ss = ss.substr(i+1, ss.length()-i);
                    break;
                }
            }
            
            ss += a;
            //cout << ss << endl;
            if (ss.size() > max_str) {
                //cout << "found max!" << ss << endl;
                max_str = ss.size();
            }
        }
        
        return max_str;
    }
};