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
//https://github.com/ruippeixotog/google-code-jam-2018/blob/master/round1a/bit-party.cpp
#include <iostream>
#include <algorithm>    // std::sort
#include <vector>
#include <cmath>
#include <queue>

#define MAXC 1000
using namespace std;

int m[MAXC], s[MAXC], p[MAXC];
int items[MAXC];

int main()
{
    int T, n;
    long long mtime;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int R, B, C; // # robot, # bits, # cashiers
    
        std::cin >> R >> B >> C;

        for (int i = 0; i < C; i++) {
            std::cin >> m[i] >> s[i] >> p[i];
        }
        long long min_time = 2, max_time = (long long) 2e18;

        while (min_time < max_time) {
            mtime = (max_time + min_time) / 2;

            for (int i = 0; i < C; i++) {
                items[i] = (int) max(0LL, min((long long) m[i], (mtime - p[i]) / s[i]));
            }

            sort(items, items + C);
            
            long long cnt = 0;
            
            for (int i = 0; i < R; i++)
                cnt += items[C - i - 1];
                
            if (cnt >= B)
                max_time = mtime;
            else
                min_time = mtime + 1;
        }

        printf("Case #%d: %lld\n", T, min_time);
        T++;
    }
    
    return 0;
}