// Longest Substring with At Most K Distinct Characters

/*
Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.
*/

// my solution
class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        vector<int> freq(256, 0);
        
        int res = 0, distinct = 0;
        
        for (int i = 0, j = 0; j < s.size(); j++) {
            if (freq[s[j]]++ == 0)
                distinct++;
            
            while (distinct > k) {
                if (--freq[s[i++]] == 0)
                    distinct--;
            }
            
            res = max(res, j - i + 1);
        }
        
        return res;
    }
};