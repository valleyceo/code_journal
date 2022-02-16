// You can go your own way

/*
Problem link:
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da
*/

// my solution
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

/* Note:
- Given NxN grid and a Lydia's path
- Start in northwest cell and reach southeast cell
- You can only move east or south but not leave the grid
- Find a path that does not cross Lydia's path

Test case:
1: 2, SE => ES
2: 5, EESSSESE => SEEESSES

Limitations:
T1: 2 < N < 10
T2: 2 < N < 1000
T3: 2 < N < 50000

Solution:
invert all S<=>E
*/