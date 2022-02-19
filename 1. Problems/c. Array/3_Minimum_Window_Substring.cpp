// Minimum Window Substring

/*
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
*/

// my solution - optimal
class Solution {
public:
    string minWindow(string s, string t) {
        vector<int> map(128, 0);
        int counter = t.size(); // substring checker
        int min_head = 0, begin=0, end = 0; // head and tail index
        int d = INT_MAX; // length of substring
        
        // create hash
        for (char a : t)
            map[a]++;
         
        while (end < s.size()) {
            
            if (map[s[end++]]-- > 0)
                counter--;
            
            // when valid
            while (counter == 0) {
                if (end - begin < d) {
                    d = end - begin;
                    min_head = begin;
                }
                
                if (map[s[begin++]]++ == 0)
                    counter++;
            }
        }
        
        return (d == INT_MAX) ? "" : s.substr(min_head, d);
    }
};