// Short Encoding of Words

/*
Given a list of words, we may encode it by writing a reference string S and a list of indexes A.

For example, if the list of words is ["time", "me", "bell"], we can write it as S = "time#bell#" and indexes = [0, 2, 5].

Then for each index, we will recover the word by reading from the reference string from that index until we reach a "#" character.

What is the length of the shortest reference string S possible that encodes the given words?

Example:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: S = "time#bell#" and indexes = [0, 2, 5].
Note:

1 <= words.length <= 2000.
1 <= words[i].length <= 7.
Each word has only lowercase letters.
*/

// my solution
// https://leetcode.com/problems/short-encoding-of-words/discuss/125819/C++-reverse-the-word-and-count

class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        set<string> s;
        
        for (auto& word : words) {
            reverse(word.begin(), word.end());
            s.insert(word);
        }
        
        int res = 0;
        string prev;
        
        for (auto word : s) {
            // if new longer word is same prefix as prev word, then don't count
            if (word.substr(0, prev.size()) != prev) {
                res += prev.size() + 1; // add 1 (# btw words)
            }
            prev = word;
        }
        res += prev.size() + 1;
        return res;
    }
};

/*
explanation
- Reverse each words because finding prefix is easier.
- Every reference words ends with # (add 1 on each max words)
- After reversing and sorting, count the longest in the same prefix group.
- You do not need to count the subwords b/c we are looking for the shortest reference string.
*/