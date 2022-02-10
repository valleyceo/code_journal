// Reverse Words in a String

/*
Given an input string, reverse the string word by word.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Update (2015-02-12):
For C programmers: Try to solve it in-place in O(1) space.

click to show clarification.

Clarification:
What constitutes a word?
A sequence of non-space characters constitutes a word.
Could the input string contain leading or trailing spaces?
Yes. However, your reversed string should not contain leading or trailing spaces.
How about multiple spaces between two words?
Reduce them to a single space in the reversed string.
*/

// my solution
class Solution {
public:
    void reverseWords(string &s) {
        // clean front
        while (s[0]==' ')
            s.erase(s.begin());
        
        // reverse
        reverse(s.begin(), s.end());
        
        int idx = 0;
        while (idx < s.size()) {
            // find first letter of word
            while (s[idx] == ' ') 
                s.erase(s.begin() + idx);
            
            int start = idx;
            
            // find end of word
            while (s[idx] != ' ' && idx < s.size())
                idx++;
            
            int end = idx;
            
            // reverse word
            reverse(s.begin()+start, s.begin()+end);
            
            idx++;
        }
        
        // output
        cout << s << endl;
        
        return;
    }
};