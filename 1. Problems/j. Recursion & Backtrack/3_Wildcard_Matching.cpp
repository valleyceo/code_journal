// Wildcard Matching

/*
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
*/

// my solution
// https://leetcode.com/problems/wildcard-matching/discuss/17811/My-three-C++-solutions-(iterative-(16ms)-and-DP-(180ms)-and-modified-recursion-(88ms))

class Solution {
public:
    bool isMatch(string s, string p) {
        int slen = s.size();
        int plen = p.size();
        int i, j;
        int iStar = -1;
        int jStar = -1;
        
        for (i = 0, j = 0; i < slen; ++i, ++j) {
            if (p[j] == '*') {
                iStar = i;
                jStar = j;
                --i;
            } else {
                if (p[j] != s[i] && p[j] != '?') {
                    if (iStar >= 0) {
                        i = iStar++;
                        j = jStar;
                    } else {
                        return false;
                    }
                }
            }
        }
        
        while(p[j] == '*')
                ++j;
        
        return j == plen;
    }
};