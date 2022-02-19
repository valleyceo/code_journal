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

// my solution - topological sorting
//source: https://leetcode.com/problems/alien-dictionary/discuss/70303/Very-easy-Solution20ms-C++

class Solution {
public:
    string alienOrder(vector<string>& words) {
        unordered_map<char,unordered_set<char>> edges;
        string res;
        unordered_set<char> u_set;
        
        // create edges
        for (int i = 0; i < words.size(); i++) {
            // add to set
            for (int k = 0; k < words[i].size(); k++)
                u_set.insert(words[i][k]);
            
            // create edges
            for (int j = i+1; j < words.size(); j++) {
                int k = 0;
                
                while (k < words[i].size() && k < words[j].size() && words[i][k] == words[j][k]) 
                    k++;
                
                if (k < words[i].size() && k < words[j].size()) {
                    edges[words[j][k]].insert(words[i][k]);
                }
            }
        }
        
        // add * on each edges
        for (auto a : u_set) {
            if (edges.find(a) == record.end())
                edges[a].insert('*');
        }
        
        int n = u_set.size();

        // while u_set is not empty
        while(n > 0){
            char cur;

            // iterate through each edges
            for (auto iter = edges.begin(); iter != edges.end(); iter++) {

                // if current edge has only * or size of zero
                if ((iter->second.size() == 1 && iter->second.find('*') != iter->second.end()) || iter->second.size() == 0) {
                    //set edge to current, append to ans, and erase
                    cur = iter->first;
                    res.push_back(cur);
                    edges.erase(iter);
                    break;
                }
            }
            
            // iterate through edges again
            for (auto iter = edges.begin(); iter != edges.end(); iter++) {
                // if current edge connects to current
                if (iter->second.find(cur) != iter->second.end())
                    // delete edge with current
                    iter->second.erase(iter->second.find(cur));
            }
            
            // decrease size
            n--;
        }
        
        // cyclic case
        if (edges.size() > 0) 
            return "";
        
        return res;
    }
};