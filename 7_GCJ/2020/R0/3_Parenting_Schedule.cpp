// Go, Gopher!

/*
Problem link:
https://codejam.withgoogle.com/2018/challenges/00000000000000cb/dashboard/0000000000007a30
*/

// my solution
// ./3_Parenting_Schedule.o < 3_0in.txt > 3_0out.txt   
// g++ -o 3_Parenting_Schedule.o 3_Parenting_Schedule.cpp

#include <iostream>
#include <string>
#include <cstring>
#include <vector>

using namespace std;

struct Event {
    int start, finish, idx;
    char user;
};

struct comp
{
    bool operator()(const Event& a, const Event& b) {
        return a.start < b.start;
    }
};

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;
    

    while (T <= n)
    {
        int N;
        string res = "";
        std::cin >> N;
        int start, end;
        int c_max = 0, j_max = 0;
        bool impossible = false;

        vector<Event> V;
        vector<int> res_array(N, 0);

        for (int i = 0; i < N; ++i) {
            std::cin >> start >> end;
            Event e = {start, end, i, 'X'};
            V.push_back(e);
        }

        sort(V.begin(), V.end(), comp());

        for (Event& e : V) {
            if (c_max <= e.start) {
                c_max = e.finish;
                e.user = 'C';
            } else if (j_max <= e.start) {
                j_max = e.finish;
                e.user = 'J';
            } else {
                impossible = true;
                break;
            }
        }
        
        if (impossible) {
            cout << "Case #" << to_string(T++) << ": " << "IMPOSSIBLE" << '\n';
        } else {
            for (auto v : V) {
                res_array[v.idx] = v.user;
            }

            for (auto c : res_array) {
                res += c;
            }

            cout << "Case #" << to_string(T++) << ": " << res << '\n';
        }
        
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