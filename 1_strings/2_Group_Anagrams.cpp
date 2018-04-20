// Group Anagrams

/*
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
*/

// my solution - optimal
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> umap;
        vector<vector<string>> ans;
        
        for (string s : strs) {
            string temp = s;
            sort(temp.begin(), temp.end());
            umap[temp].push_back(s);
        }
        
        for (auto m : umap) {
            vector<string> str_vec = m.second;
            ans.push_back(str_vec);
        }
        
        return ans;
    }
};