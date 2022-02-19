// Valid Palindrome

/*
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
*/

// my solution
class Solution {
public:
    bool isPalindrome(string s) {
        string ns;
        
        for (char a: s){
            if (a-'a'>= 0 && a-'a' < 26) {
                ns += a;
            } else if (a-'A'>= 0 && a-'A' < 26) {
                ns += (char)((int)a+32);
            } else if (a-'0'>= 0 && a-'0' < 10) {
                ns += a;
            }
        }
        
        for (int i=0; i<ns.length()/2; i++) {
            if (ns[i] != ns[ns.length()-1-i])
                return false;
        }
        
        return true;
    }
};