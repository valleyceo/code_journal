// Valid Anagram

/*
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
*/

// my solution
class Solution {
public:
    bool isAnagram(string s, string t) {
        
        if (s.length() != t.length()) {
            return false;
        }
        
        int s1[26] = {0};
        
        for (int i=0; i<s.length(); i++) {
            s1[s[i] - 'a'] += 1;
            s1[t[i] - 'a'] -= 1;
        }
        
        for (int i=0; i<26; i++) {
            if (s1[i] != 0){
                return false;
            }
        }
        
        return true;
    }
};