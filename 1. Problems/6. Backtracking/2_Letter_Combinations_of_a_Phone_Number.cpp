// Letter Combinations of a Phone Number

/*
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

ex: {2: 'abc', 3: 'def', 4: 'ghi', 5: 'jkl', 6: 'mno', 7:'pqrs', 8:'tuv', 9:'wxyz'}
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
*/

// my solution
class Solution {
public:
    vector<string> letterCombinations(string digits) {
        vector<string> perm;
        unordered_map<char, string> dial = {{'2',"abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}};
        
        for (char num : digits) {
            string letters = dial[num];
            vector<string> temp;
                
            if (perm.empty()) {
                for (char a : letters) {
                    string s = "";
                    s += a;
                    temp.push_back(s);
                }
            } else {
                for (string x : perm) {
                    for (char a : letters) {
                        temp.push_back(x+a);
                    }
                }
            }
            
            perm = temp;
            
            }
        
        return perm;
        
    }
};