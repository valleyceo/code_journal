// Overexcited fan

/*
Problem:
- Infinite street grids with intersections, 1 grid unit
- Tour starts at (X, Y), moves a certain route
- You move 1 minute/block
- You can stop and wait or move towards tour location

Question:
- Is it possible to meet tour?

*/

// my solution
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int X, Y;
        cin >> X >> Y;

        string S;
        cin >> S;

        int time = 0;
        int res = -1;

        for (auto dir : S) {
            time++;

            if (dir == 'N') {
                Y++;
            } else if (dir =='S') {
                Y--;
            } else if (dir =='W') {
                X--;
            } else {
                X++;
            }

            //printf("Time: %d, X: %d, Y:%d\n", time, X, Y);

            if (time >= abs(X) + abs(Y)) {
                res = time;
                break;
            }
        }

        if (res == -1) {
            cout << "Case #" << to_string(T++) << ": " << "IMPOSSIBLE"  << '\n';
        } else {
            cout << "Case #" << to_string(T++) << ": " << res << '\n';
        }
        
    }
    
    return 0;
}
