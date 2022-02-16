// Expogo

/*
Problem:
- Expogo stick, increasingly large jumps
- Start at (0,0), try to reach (X, Y) with few jumps as possible
- Must land at exact point
- Each jump can be jumped in 4 direction
- jump size doubles, meaning size of i-th jump equals 2^(i-1)

Question:
- Given goal point (X, Y), determine if it's possible to reach.
- If multiple solution exist, jump with the fewest possible.

Solution:
- Jump is impossible if X + Y is even, since jump sequence is 1, 2, 4, 8, ...
- Move 1 to the odd direction
    - You have 2 possible direction
    - Go to the 1 jump direction that results in next X/2 + Y/2 to be odd
    - If both works, use the one that moves closer to origin.
- Divide X and Y by 2 and repeat step until X+Y=0

useful links:
- https://sohojeprogramming.blogspot.com/2020/04/google-code-jam-2020-1b-expogo.html
*/

// my solution
#include <iostream>
#include <vector>
#include <set>

using namespace std;

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int x, y;
        std::cin >> x >> y;
        string res = "";

        while (x != 0 || y != 0) {
            if ( (x + y) % 2 == 0) {
                res = "IMPOSSIBLE";
                break;
            }

            if (abs(x) + abs(y) == 1) {
                if (x==1) res += "E";
                if (x==-1) res += "W";
                if (y==1) res += "N";
                if (y==-1) res += "S";
                x = y = 0;
            }

            if (x % 2) {
                if (((x-1)/2 + y/2) % 2) {
                    res += "E";
                    x--;
                } else {
                    res += "W";
                    x++;
                }
            }

            if (y % 2) {
                if ((x/2 + (y-1)/2) % 2) {
                    res += "N";
                    y--;
                } else {
                    res += "S";
                    y++;
                }
            }

            x = x/2;
            y = y/2;
        }

        cout << "Case #" << to_string(T++) << ": " << res << '\n';
    }
    
    return 0;
}