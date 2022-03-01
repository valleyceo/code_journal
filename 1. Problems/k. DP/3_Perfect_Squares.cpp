// Perfect Squares

/*
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9.
*/

// my solution
// https://leetcode.com/problems/perfect-squares/discuss/71488/Summary-of-4-different-solutions-(BFS-DP-static-DP-and-mathematics)

class Solution {
public:
    int numSquares(int n) {
        if (n <= 0)
            return 0;
        
        vector<int> ct(n + 1, INT_MAX);
        ct[0] = 0;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j * j <= i; j++) {
                ct[i] = min(ct[i], ct[i - j * j] + 1);
            }
        }
        return ct.back();
    }
};