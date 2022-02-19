// First Unique Character in a String

/*
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
*/

// my solution
class Solution {
public:
    int firstUniqChar(string s) {
        if (s.length() == 0){
            return -1;
        }
        
        if (s.length() == 1){
            return 0;
        }
        
        bool dup;
        
        for (int i=0; i<s.length(); i++){
            dup = false;
            
            for (int j=0; j<s.length();j++) {
                
                if (i!=j && s[i] == s[j]){
                    dup = true;
                    break;
                }
            }
            
            if (dup == false){
                return i;
            }
        }
        return -1;
    }
};