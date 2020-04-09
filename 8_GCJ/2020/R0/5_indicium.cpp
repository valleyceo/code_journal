// Indicium

// g++ -o 5_indicium.o 5_indicium.cpp  
//./5_indicium.o < 5_0in.txt > 5_0out.txt

// my solution
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;


void printSquare(vector<vector<int> >& M) {
    for (int i = 0; i < M.size(); ++i) 
    {
        string s = "";
        for (int j = 0; j < M.size(); ++j) {
            s += j == (M.size()-1) ? to_string(M[i][j]) + "\n" : to_string(M[i][j]) + " ";
        }
        cout << s;
    }
}

bool findSquare(vector<vector<int> >& M, int r, int c, int N, int K) {

    for (int i = 0; i < c; ++i) {
        if (M[r][i] == M[r][c])
            return false;
    }

    for (int i = 0; i < r; ++i) {
        if (M[i][c] == M[r][c])
            return false;
    }

    int sum = 0;

    if (r == c) {
        for (int i = 0; i <= r; ++i) {
            sum += M[i][i];
            if (sum > K)
                return false;
        }
    }

    if (r == N - 1 && c == N - 1) {
        if (sum == K){
            return true;
        } else {
            return false;
        }
    }

    bool found = false;

    for (int i = 1; i <= N; ++i) {
        if (c < N - 1) {
            M[r][c+1] = i;
            found = findSquare(M, r, c + 1, N, K);
        } else if (c == N - 1 && r < N - 1) {
            M[r+1][0] = i;
            found = findSquare(M, r + 1, 0, N, K);
        }

        if (found) {
            return true;
        }
    }

    return false;
}


int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;
    
    while (T <= n)
    {
        int N, K;
        bool f;
        std::cin >> N >> K;
        vector<vector<int> > res(N, vector<int>(N, 0));
        
        for (int i = 1; i <= N; ++i) {
            res[0][0] = i;
            f = findSquare(res, 0, 0, N, K);

            if (f)
                break;
        }
        
        string ans = f ? "POSSIBLE" : "IMPOSSIBLE";
        cout << "Case #" << to_string(T++) << ": " << ans << '\n';

        if (f)
            printSquare(res);
    }
    
    return 0;
}



/*
Note:
- Pangram: phrase that use each letter of english at least once
- Encryption scheme: 
    - choose 26 different prime numbers smaller than N
    - Sort primes in increasing order and assign in order of A, B, C, ...
    - Message sent in order of P1*P2, P2*P3, P3*P4, ..., PN-1*PN

Test Case:
1: 103(max prime), 31(message length), 217 1891 ... => CJQUIZ...

Limitations:
Tests = 1-100
Memory = 1GB
L (message length) = 25-100
T1: 101 < N < 10000
T2: 101 < N < 10^100

Solution:
- Semi prime factorization: http://www2.mae.ufl.edu/~uhk/QUICK-SEMI-PRIME-FACTORING.pdf
-> use euclidean algorithm (greatest common divisor)
*/