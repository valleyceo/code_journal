// Generate Parentheses

/*
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
*/

// my solution
class Solution {
public:
    vector<string> ans;
    
    vector<string> generateParenthesis(int n) {
        recurse("", n, 0);
        
        return ans;
    }
    
    void recurse(string s, int n, int rem) {
        if (n==0 && rem==0) {
            ans.push_back(s);
            return;
        }
        
        if (n > 0) {
            recurse(s + "(", n-1, rem+1);
        }
        
        if (rem > 0) {
            recurse(s + ")", n, rem-1);
        }
    }
};