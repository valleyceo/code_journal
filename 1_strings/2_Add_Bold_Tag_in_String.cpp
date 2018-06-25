// Add Bold Tag in String

/*
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:
The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
*/

// my solution
class Solution {
public:
    string addBoldTag(string s, vector<string>& dict) {
        vector<int> dp(s.length(), 0);
        string res = "";
        
        for (auto d : dict) {
            size_t pos = s.find(d);
            
            while(pos != string::npos)
            {
                for (int i = pos; i < pos + d.size(); i++)
                    dp[i] = 1;
                pos = s.find(d, pos + 1);
            }
        }
        
        bool flag = false;
        
        for (int i = 0; i < s.length(); i++) {
            if (flag == false && dp[i] == 1) {
                flag = true;
                res += "<b>";
                res += s[i];
            } else if (flag == true && dp[i] == 0) {
                flag = false;
                res += "</b>";
                res += s[i];
            } else {
                res += s[i];
            }
        }
        
        if (flag)
            res += "</b>";
        
        return res;
    }
};