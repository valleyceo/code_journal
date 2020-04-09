// Title

/*
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
*/

// my solution - Optimal, time complexity: O(NlogN), space complexity: O(N)
class Solution {
public:
    vector<int> numSmallerByFrequency(vector<string>& queries, vector<string>& words) {
        vector<int> W, res;
        
        for (auto w : words) {
            W.push_back(getNum(w));
        }
        
        sort(W.begin(), W.end());
        
        for (auto s : queries) {
            int tempNum = getNum(s);
            int idx = W.end() - upper_bound(W.begin(), W.end(), tempNum);
            
            res.push_back(idx);
        }
        
        return res;
    }
    
    int getNum(string s) {
        int ct = 0;
        int ch = 'z' + 1;
        for (auto c : s) {
            if (c < ch) {
                ct = 1;
                ch = c;
            } else if (c == ch) {
                ct++;
            }
        }
        
        return ct;
    }
};