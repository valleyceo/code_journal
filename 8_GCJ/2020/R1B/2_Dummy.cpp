// Edgy Baking

/*
Link:
https://codejam.withgoogle.com/2018/challenges/0000000000007883/dashboard/000000000002fff6
*/

// my solution
#include <iostream>
#include <algorithm>    // std::sort
#include <vector>
#include <cmath>
#include <queue>

#define MAX 25010

// cookie structure
struct cookie {
    int w, h;
};

cookie cookies[110];
double dp[MAX];
double DBL_MIN = -1e10;
double L;

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int n; // # cookies
        double P; // max desired perimeter
        int w, h;
        int sum = 0;
        double ans = 0.0;
        double mx;

        std::cin >> n >> P;

        for (int i = 1; i <= n; i++) {
            std::cin >> w >> h;

            // assign, coo
            if (h > w) {
                cookies[i].h = w;
                cookies[i].w = h;
            } else {
                cookies[i].h = h;
                cookies[i].w = w;                
            }

            sum += cookies[i].h;
            P -= 2 * (cookies[i].h + cookies[i].w);
            ans += 2 * (cookies[i].h + cookies[i].w);
        }

        P /= 2; // cut in half (since cutting creates 2 * L)

        for (int i = 1; i <= sum; i++)
            dp[i] = DBL_MIN;

        int nows = 0;

        for (int i = 1; i <= n; i++) {
            L = sqrt((double)(cookies[i].h * cookies[i].h + cookies[i].w * cookies[i].w)); // diag

            for (int j = nows; j >= 0; j--) {
                if (dp[j + cookies[i].h < dp[j] + L]) 
                    dp[j + cookies[i].h] = dp[j] + L;
            }

            nows += cookies[i].h;
        }
        /*
        cout << endl;
        cout << "height : ";
        for (int i = 0; i <= n; i++){
            cout << cookies[i].h << " ";
        }
        cout << endl;
        cout << "width : ";
        for (int i = 0; i <= n; i++){
            cout << cookies[i].w << " ";
        }
        cout << endl;
        cout << "dp : ";
        for (int i = 0; i <= n; i++){
            cout << dp[i] << " ";
        }
        cout << endl;
        */
        
        mx = DBL_MIN;
        
        for (int i = 0; i <= sum; i++) {
            if (i > P)
                break;

            if (dp[i] >= P) {
                mx = P * 2;
                break;
            } else {
                if (mx < dp[i] * 2)
                    mx = dp[i] * 2;
            }

        }

        ans += mx;
        printf("Case #%d: %.12lf\n", T, ans);
        T++;
    }
    
    return 0;
}

/* Note:
- Given 1-M gophers, emerge 1 by 1, chooses one of windmills (independent, uniform) and rotates blade counterclockwise by 1
- Windmill of 2 < B < 18 (for each holes)
- Blades 1-B clockwise

- Each night before sleep, turn off windmills and set blade 0 pointing downward
- Figure out how many gophers there are given N nights

Limitation:
T (test set): 1~20
N (number of nights) = 365 and 7
M (max number of gophers) = 100 and 10^6

Example interaction:
out 2 2 2 2 18 3 3 3 3 3 3 4 4 4 4 5 2 2 ->
in  0 0 0 0 0 0 1 2 1 0 1 2 0 0 0 0 1 0

*/