// Bit Party

/*
Link:
https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard/000000000002fff6

- R robot shoppers
- Each buys B "bits" of items
- C cashiers where I-th cashier:
	* Accept max Mi items per customer
	* Take Si seconds to scan each item
	* Spend Pi seconds handling payment
- Interaction time = Si x B + Pi

Q: Try to purchase all as quickly as possible

Input:
1. Test cases T
2. Each begins with three int. R, B, C
3. C lines of ith cashier - each has three int of Mi, Si, Pi

*/

// my solution
#include <iostream>
#include <string>
#include <vector>

using namespace std;
void printM(vector<vector<bool> > M) {
    cout << "Printing Board" << endl;
    for (int i = 0; i < M.size(); ++i) {
        for (int j = 0; j < M[0].size(); ++j) {
            cout << M[i][j] << " ";
        }
        cout << endl;
    }
}

void printS(vector<string> seq) {
    cout << "printing seq " << endl;
    for (int i = 0; i < seq.size(); ++i) {
        cout << seq[i] << " ";
    }
    cout << endl;
}

bool recurse(vector<vector<bool> >& M, int r, int c, vector<string>& seq) {

    seq.push_back(to_string(r+1) + " " + to_string(c+1));
    M[r][c] = true;

    //printM(M);
    //printS(seq);

    if (M.size()*M[0].size() == seq.size())
        return true;

    for (int i = 0; i < M.size(); ++i) {
        if (r == i)
            continue;

        for (int j = 0; j < M[0].size(); ++j) {
            if (c == j)
                continue;

            if (M[i][j] == true)
                continue;

            if (r-c == i-j || r+c == i+j)
                continue;

            bool out = recurse(M, i, j, seq);
            if (out)
                return true;
        }
    }

    M[r][c] = false;
    seq.pop_back();

    return false;
}

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int R, C;
        cin >> R >> C;
        vector<vector<bool> > M(R, vector<bool>(C, false));
        vector<string> seq;
        int r = 0;
        int c = 0;
        int depth = 1;
        bool out = recurse(M, r, c, seq);

        if (out) {
            cout << "Case #" << to_string(T++) << ": " << "POSSIBLE"  << '\n';
            for (int i = 0; i < seq.size(); ++i) {
                cout << seq[i] << endl;
            }
        } else {
            cout << "Case #" << to_string(T++) << ": " << "IMPOSSIBLE"  << '\n';
        }
        
    }
    
    return 0;
}

/* Note:
My solution:
- create 1-400 array(unordered set) of indices and shuffle
- starting from first index, add value to the matrix
- if value is not legit move, then reshuffle until you get correct
- if remaining moves are x (20~30?), then finish rest with back propagation
    - Since 5x5 propagation is computationally fast
*/