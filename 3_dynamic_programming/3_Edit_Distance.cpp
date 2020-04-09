// Edit Distance

/*
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')
Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
*/

// my solution
class Solution {
public:
    int ComputeDistance(const string& A, int A_idx, const string& B, int B_idx,
					    vector<vector<int>>* ptr) {
		vector<vector<int>>& distance = *ptr;

		if (A_idx < 0) {
			return B_idx + 1;
		} else if (B_idx < 0) {
			return A_idx + 1;
		}

		if (distance[A_idx][B_idx] == -1) {
			if (A[A_idx] == B[B_idx]) {
				// no actions move diagonally
				distance[A_idx][B_idx] = ComputeDistance(A, A_idx-1, B, B_idx-1, ptr);
			} else {
	            // traverse all options
				int substitute_last = ComputeDistance(A, A_idx-1, B, B_idx-1, ptr);
				int add_last = ComputeDistance(A, A_idx-1, B, B_idx, ptr);
				int delete_last = ComputeDistance(A, A_idx, B, B_idx-1, ptr);
				
				distance[A_idx][B_idx] = 1 + min({substitute_last, add_last, delete_last});
			}
		}

		return distance[A_idx][B_idx];
    }
    
    int minDistance(string A, string B) {
        vector<vector<int>> distance_btw_pref(A.length(), vector<int> (B.length(), - 1));

        // Compute Levenshtein Distance
	    return ComputeDistance(A, A.length()-1, B, B.length()-1, 
                        make_unique<vector<vector<int>>>(A.length(), vector<int>(B.length(), -1)).get());
    }
};