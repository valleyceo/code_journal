// Edgy Baking

/*
Problem:
- Circular pancakes, all same size
- Chop them into slices
- N slices ith slice has Ai nanodegree (10^-9)
- D diners want same size of slize

Question:
- Determine smallest total number of cuts needed

Input:
- N number of slices you currently have
- D number of diners
- A1, A2, ..., Ai -> internal angle of ith slice

solution:
- sort and count (sort by highest count, then lowest)
- starting with smallest cake, check how many 
*/

#include <iostream>
#include <string>
#include <vector>

using namespace std;

void printS(vector<string> seq) {
    cout << "printing seq " << endl;
    for (int i = 0; i < seq.size(); ++i) {
        cout << seq[i] << " ";
    }
    cout << endl;
}

void printS(vector<bool> seq) {
    cout << "printing " << endl;
    for (int i = 0; i < seq.size(); ++i) {
        cout << seq[i] << " ";
    }
    cout << endl;
}

int recurse(vector<string> W, vector<bool>& W_check, vector<bool>& A_check, int count) {
	if (count == W.size())
		return count;

	//cout << "STAGE : "<< endl;
 	//printS(W_check);
 	//printS(A_check);

	int idx, maxl, max_count = count;

    for (int i = 0; i < W.size(); ++i) {
        for (int j = 0; j < W.size(); ++j) {
        	if (i == j)
        		continue;

        	if (W_check[i] || W_check[j])
        		continue;


        	W_check[i] = true;
        	W_check[j] = true;
        	idx = 0;
        	maxl = min(W[i].size(), W[j].size());

        	while (idx < maxl && W[i][idx] == W[j][idx]) {
        		
        		int a = W[i][idx]-'A';
        		idx++;

        		//cout << a << endl;
        		if (A_check[a])
        			continue;

        		A_check[a] = true;
        		max_count = max(recurse(W, W_check, A_check, count + 2), max_count);

        		if (max_count == W.size())
        			return max_count;

        		A_check[a] = false;
        	}
        	W_check[i] = false;
        	W_check[j] = false;
        }
    }

    return max_count;
}

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int L;
        cin >> L;

        vector<string> W;
        string w;

        while (L-- > 0) {
        	cin >> w;
        	reverse(w.begin(), w.end());
        	W.push_back(w);
        }
        //printS(W);

        vector<bool> W_check(W.size(), false);
        vector<bool> A_check(26, false);

        int count = recurse(W, W_check, A_check, 0);

        cout << "Case #" << to_string(T++) << ": " << count  << '\n';
        
    }
    
    return 0;
}