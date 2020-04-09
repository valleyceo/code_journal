// Alien Rhyme
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

/* Note:
- Alien poetry
- Each word has accent on one position (letter) 
- Two words rhyme if both of their accent-suffixes are equal (part of the word starting from accented letter)
- Ex: 
	PROL + TARPOL: 
		rhyme if accented letter in both are O or L
		unrhyme if accented letters are R/R, R/P, O/L

- Given N words
- Find the largest number of words that can be arranged into pairs

Test Case:
1. TARPOL PROL -> 2
2. TARPOR PROL TARPRO -> 0
3. CODEJAM JAM HAM NALAM HUM NOLOM -> 6
4. PI HI WI FI -> 2

*/