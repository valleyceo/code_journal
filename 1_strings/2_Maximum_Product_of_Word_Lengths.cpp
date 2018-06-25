// Maximum Product of Word Lengths

/*
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
*/

// my solution
class Solution {
public:
    int maxProduct(vector<string>& words) {
        if (words.size() == 0) return 0;
        
        vector<int> bitmap (words.size(), 0);
        int max_len = 0;
        
        for (int i = 0; i < words.size(); ++i)
            for (auto a : words[i])
                bitmap[i] |= (1 << a - 'a');
        
        for (int i = 0; i < words.size() - 1; ++i)
            for (int j = i + 1; j < words.size(); ++j)
                if ((words[i].length() * words[j].length() > max_len) && ((bitmap[i] & bitmap[j]) == 0))
                    max_len = words[i].length() * words[j].length();
        
        return max_len;
    }
};