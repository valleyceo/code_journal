// Reverse Words in a String III

/*
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Note: In the string, each word is separated by single space and there will not be any extra space in the string.
*/

// my solution
class Solution {
public:
    string reverseWords(string s) {
        int idx = 0;
        
        for (int i = 0; i < s.length(); i++) {
            if (s[i] == ' ') {
                for (int j = 0; j < (i - idx) / 2; j++)
                    swap(s[idx + j], s[i - j - 1]);
                
                idx = i+1;
            }
        }
        
        // final loop
        for (int j = 0; j < (s.length() - idx) / 2; j++)
            swap(s[idx + j], s[s.length() - j - 1]);
        
        return s;
    }
};