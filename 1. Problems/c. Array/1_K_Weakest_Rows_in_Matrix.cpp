// LC 1337. The K Weakest Rows in a Matrix

/*
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians), return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand in the frontier of a row, that is, always ones may appear first and then zeros.

Example 1:

Input: mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
Output: [2,0,3]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 2 
row 1 -> 4 
row 2 -> 1 
row 3 -> 2 
row 4 -> 5 
Rows ordered from the weakest to the strongest are [2,0,3,1,4]
Example 2:

Input: mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
Output: [0,2]
Explanation: 
The number of soldiers for each row is: 
row 0 -> 1 
row 1 -> 4 
row 2 -> 1 
row 3 -> 1 
Rows ordered from the weakest to the strongest are [0,2,3,1]
*/

// my solution - O(N^2) time complexity,  O(k) space complexity, Optimal
typedef pair<int, int> pi;

class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        priority_queue<pi, vector<pi>, greater<pi> > pq;
        vector<int> res;
                
        for (int i = 0; i < mat.size(); ++i) {
            int ct = 0;
            for (int j = 0; j < mat[i].size(); ++j) {
                if (mat[i][j] == 0)
                    break;
                
                ct++;
            }
            
            pq.push(make_pair(ct, i));
        }
        
        while (!pq.empty() && k--) {
            res.push_back(pq.top().second);
            pq.pop();
        }
        
        return res;
    }
};