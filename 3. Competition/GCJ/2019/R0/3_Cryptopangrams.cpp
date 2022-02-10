// Go, Gopher!

/*
Problem link:
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30
*/

// my solution
// run: g++ q3.cpp -std=c++14 -pthread -O3 -o q3.out
// python testing_tool.py ./q3.out

#include <iostream>
#include <string>

using namespace std;

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int L, Len;
        string N;
        string res = "";

        cin >> L;

        if (L > 1) {
            cin >> N;
        }
        
        Len = 2 * L - 2;

        for (int i = 0; i < Len; ++i) {
            if (N[i] == 'S') {
                res += 'E';
            } else {
                res += 'S';
            }
        }

        cout << "Case #" << to_string(T++) << ": " << res  << '\n';
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