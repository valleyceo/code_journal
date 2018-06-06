// Reverse Vowels of a String

/*
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
*/

// my solution
class Solution {
public:
    string reverseVowels(string s) {
        string vowels = "aeiouAEIOU";
        int start = 0;
        int end = s.length()-1;
        while (start < end) {
            while (vowels.find(s[start]) == vowels.npos) start++;
            
            while (vowels.find(s[end]) == vowels.npos) end--;
            
            if (start < end) swap(s[start++], s[end--]);
        }
        
        return s;
    }
};

/* Alternative
class Solution {
public:
    string reverseVowels(string s) {
        int i = 0, j = s.size() - 1;
        while (i < j) {
            i = s.find_first_of("aeiouAEIOU", i);
            j = s.find_last_of("aeiouAEIOU", j);
            if (i < j) {
                swap(s[i++], s[j--]);
            }
        }
        return s;
    }
};
*/