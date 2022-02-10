// Pascal's Triangle II

/*
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
*/

// my solution
class Solution {
public:
    int binomialCoeff(int n, int k) {
        long res = 1;
        
        if (k > n - k)
            k = n - k;
        
        for (int i = 0; i < k; ++i) {
            res *= (n - i);
            res /= (i + 1);
        }
        
        return (int)res;
    }
    
    vector<int> getRow(int rowIndex) {
        vector<int> res (rowIndex + 1, 1);
        
        for (int i = 1; i < rowIndex; i++) {
            
            res[i] = binomialCoeff(rowIndex, i);
        }
        
        return res;
    }
};