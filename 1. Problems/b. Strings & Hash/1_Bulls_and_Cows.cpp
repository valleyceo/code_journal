// Bulls and Cows

/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
*/

// my solution
class Solution {
public:
    string getHint(string secret, string guess) {
        vector<int> hash(10);
        string res = "";
        int a = 0, b = 0;

        for (int i = 0; i < secret.length(); ++i){
            hash[secret[i] - '0']++;
        }

        // bulls
        for (int i = 0; i < secret.length(); ++i) {
            if (secret[i] == guess[i]) {
                a += 1;
                hash[secret[i] - '0']--;
            }
        }

        // cows
        for (int i = 0; i < secret.length(); ++i) {
           if (secret[i] != guess[i] && hash[guess[i] - '0'] > 0 ) {
                b += 1;
                hash[guess[i] - '0']--;
            }
        }

        return to_string(a) + "A" + to_string(b) + "B";
    }
};
