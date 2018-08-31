// Regular Expression Matching

/*
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
*/

// my solution - unoptimal, time: exponential
class Solution {
public:
    bool recurse(string& s, string& p, int si, int pi) {
        // base case
        if (si == s_len && pi == p_len)
            return true;
        
        if (si > s_len || pi > p_len)
            return false;
        
        if (pi >= p_len || (pi == p_len-1 && p[pi] == '*'))
            return false;
        
        // recurse
        bool res = false;
        
        if (s[si] == p[pi] || p[pi] == '.') {
            res |= recurse(s, p, si+1, pi+1);
            
            if (res) return true;
        }
        
        if (p[pi+1] == '*') {
            res |= recurse(s, p, si, pi+2);
            if (res) return true;
            
            if (s[si] == p[pi] || p[pi] == '.') {
                res |= recurse(s, p, si+1, pi);
            }
        }
        
        return res;
    }
    
    bool isMatch(string s, string p) {
        // string empty check
        s_len = s.length();
        p_len = p.length();
        
        return recurse(s, p, 0, 0);
    }
    
private:
    int s_len, p_len;
};