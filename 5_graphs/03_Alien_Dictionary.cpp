// Alien Dictionary

/*
There is a new alien language which uses the latin alphabet. However, the order among letters are unknown to you. You receive a list of non-empty words from the dictionary, where words are sorted lexicographically by the rules of this new language. Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,

[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
The correct order is: "wertf".

Example 2:
Given the following words in dictionary,

[
  "z",
  "x"
]
The correct order is: "zx".

Example 3:
Given the following words in dictionary,

[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".

Note:
You may assume all letters are in lowercase.
You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.
*/

// my solution
//source: https://leetcode.com/problems/alien-dictionary/discuss/70303/Very-easy-Solution20ms-C++

class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char,unordered_set<char>> record;
        string res;
        unordered_set<char> alphbet;
        
        for (int i = 0; i < words.size(); i++) {
            for (int k = 0; k < words[i].size(); k++)
                alphbet.insert(words[i][k]);
            
            for (int j = i+1; j < words.size(); j++) {
                int k = 0;
                
                while (k < words[i].size() && k < words[j].size() && words[i][k] == words[j][k]) 
                    k++;
                
                if (k < words[i].size() && k < words[j].size()) {
                    record[words[j][k]].insert(words[i][k]);
                }
            }
        }
        
        for (auto ch : alphbet) {
            if (record.find(ch) == record.end())
                record[ch].insert('*');
        }
        
        int n = alphbet.size();

        while(n > 0){
            char cur;
            for (auto iter = record.begin(); iter != record.end(); iter++) {
                if ((iter->second.size() == 1 && iter->second.find('*') != iter->second.end()) || iter->second.size() == 0) {
                    cur = iter->first;
                    res.push_back(cur);
                    record.erase(iter);
                    break;
                }
            }
            
            for (auto iter = record.begin();iter != record.end();iter++) {
                if (iter->second.find(cur) != iter->second.end())
                    iter->second.erase(iter->second.find(cur));
            }
            
            n--;
        }
        
        // cyclic case
        if (record.size() > 0) 
            return "";
        
        return res;
    }
};