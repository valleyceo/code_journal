// A Whole New World 

/*
Link: 
https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard

Note:
- N distinct L length words
- Each tile contains alphabet and number(1-L)
- a word consists of letters spelled out by L tiles (1-L) in order
- find permutation word that is in order (inc number)

Input:
- N L
- #N of words

Output:
- '-' or 'permuted word'

Solution:

*/

// my solution
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

// global variables
int tries, N, L;

bool permute_word(int idx, string& word, vector< vector<bool> > word_map, vector<string> words) {
	// base case (idx at end)
    if (idx == L) {
        if (binary_search(words.begin(), words.end(), word)) {
            tries++;
            return false;
        } else {
            return true;
        }
    }
    
    // permute and search next
    for (int i = 0; i < 26; i++) {
  		if (!word_map[idx][i]) continue;
  		
  	    word.push_back((char)(i + 'A'));
		if (permute_word(idx + 1, word, word_map, words)) return true;
		word.pop_back();
		
		// return if tries go beyond n + 1
		if (tries > N) return false;
    }
    
    return false;
}

int main()
{
	int T, n;
	T = 1;
	
	cin >> n;

	while (T <= n)
	{
		cin >> N >> L;
		
		vector< vector<bool> > word_map(L, vector<bool>(26, false) );
		vector<string> words;
		int nw = N;
		
	    while (nw--) {
		    string S;
			cin >> S;
			words.push_back(S);
			for (int i = 0; i < S.length(); i++) {
				word_map[i][S[i]-'A'] = true;
			}
		}
		
		// sort word (for binary search)
		sort(words.begin(), words.end());
        
        // return if length is 1 (cannot perturb)
        if (L == 1) {
		    cout << "Case #" << to_string(T) << ": " << "-" << '\n'; 
		    T++;
		    continue;
		}
		
        // search and return next permuted word
		tries = 0;
		string res = "";
        if (permute_word(0, res, word_map, words))
			cout << "Case #" << to_string(T) << ": " << res << '\n';  
		else
		    cout << "Case #" << to_string(T) << ": " << "-" << '\n'; 
		T++;
	}
	
	return 0;
}