// Keyboard Row

/*
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.


American keyboard


Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
Note:
You may use one character in the keyboard more than once.
You may assume the input string will only contain letters of alphabet.
*/

// my solution
class Solution {
public:
    vector<string> findWords(vector<string>& words) {
        vector<int> map_row(26, 0);
        vector<string> res;
        string row1 = "qwertyuiop", row2 = "asdfghjkl", row3 = "zxcvbnm";
        
        for (auto a : row1)
            map_row[a-'a'] = 1;
            
        for (auto a : row2)
            map_row[a-'a'] = 2;
        
        for (auto a : row3)
            map_row[a-'a'] = 3;
        
        for (auto word : words) {
            int a = map_row[tolower(word[0])-'a'];
            bool flag = true;
            
            for (int i = 1; i < word.size(); i++) {
                if (map_row[tolower(word[i])-'a'] != a) {
                    flag = false;
                    break;
                }
            }
            
            if (flag)
                res.push_back(word);
        }
        
        return res;
    }
};