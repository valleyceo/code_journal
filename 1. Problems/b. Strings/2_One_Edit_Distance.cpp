// One Edit Distance

/*
Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
*/

// my solution
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int a = s.length();
        int b = t.length();
        
        if (a < b) {
            return isOneEditDistance(t, s);
        }
        
        if (a - b > 1)
            return false;
        
        for (int i = 0; i < b; ++i) {
            if (s[i] != t[i]) {
                return (s.substr(i+1) == t.substr(i+1) || s.substr(i+1) == t.substr(i));
            }
        }
        
        
        return (a - b == 1);
    }
};


/* Levenshtein distance
 |1 2 0 3
-+-------
1|0 1 2 3 4
2|1 0 1 2 3
1|2 1 0 2 3
3|3 2 2 1 2
  4 3 3 2 1

Optimize: since you compute row by row, and first value of new row equals the row#+1, can use only 1 row
class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        if (s == "" || t == "") {
            if (s.length() == 1 || t.length() == 1) {
                return true;
            } else {
                return false;
            }
        }
        
        vector<int> prev_row(t.length()+1, 0), new_row(t.length()+1, 0);
        
        for (int i = 0; i <= t.length(); ++i) 
            prev_row[i] = i;
        
        for (int i = 1; i <= s.length(); ++i) {
            new_row[0] = i;
            
            for (int j = 1; j <= t.length(); ++j) {
                new_row[j] = min({prev_row[j]+1, new_row[j-1]+1, prev_row[j-1] + (s[i-1] == t[j-1] ? 0 : 1)});
            }
            
            swap(new_row, prev_row);
        }
        
        return prev_row[t.length()] == 1;
    }
};

One Edit Distance optimization: No need for DP, just check for the first s[i] != t[j] and see if the rest of string is correct

*/