// Remove Invalid Parentheses

/*
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:
"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]
*/

// my solution
// https://leetcode.com/problems/remove-invalid-parentheses/discuss/75048/recommend-for-beginnersclean-C++-implementation-with-detailed-explaination

class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        int remove_left = 0;  // number of left to delete
        int remove_right = 0; // number of right to delete
        int pair = 0;         // number of pair in solution
        
        unordered_set<string> result;
        
        // count how many left/right to remove
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') 
                remove_left++;
            else if (s[i] == ')') {
                if (remove_left > 0)
                    remove_left--;
                else
                    remove_right++;
            }
        }
        
        dfs(0, 0, remove_left, remove_right, s, "", result);
        
        return vector<string>(result.begin(), result.end());
    }
    
private:
    void dfs(int pair, int index, int remove_left, int remove_right, const string& s, string solution, unordered_set<string>& result ) {
        // end condition
        if (index == s.size()){
            if (pair == 0 && remove_left == 0 && remove_right == 0)
                result.insert(solution);
            return;
        }
        
        // left-half
        if(s[index]=='(') {
            if (remove_left > 0)
                dfs(pair, index + 1, remove_left - 1, remove_right, s, solution, result);
            
            dfs(pair+1, index + 1, remove_left, remove_right, s, solution+s[index], result);
        // right-half
        } else if (s[index] == ')') {
            if (remove_right > 0)
                dfs(pair, index + 1, remove_left, remove_right - 1, s, solution, result);
            
            if (pair > 0)
                dfs(pair - 1, index + 1, remove_left, remove_right, s, solution + s[index], result);
        // non-parantheses
        } else {
            dfs(pair, index + 1, remove_left, remove_right, s, solution + s[index], result);
        }
    }
};