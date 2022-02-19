// Longest Common Prefix

/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
*/

// my solution
lass Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0 || strs[0].length() == 0){
            return "";
        }
        string ans = "";
        bool is_pref = true;
        int idx = 0;
        
        while(is_pref && idx < strs[0].length()){
            char c = strs[0][idx];
            cout << c << " : here" << endl;
            for (int i=1; i< strs.size(); i++) {
                if (idx >= strs[i].length()) {
                    is_pref = false;
                    break;
                    
                }
                
                if (strs[i][idx] != c){
                    is_pref = false;
                    break;
                }
            }
            
            if (is_pref){
                ans += c;
            }
            idx++;
        }
        
        return ans;
    }
};