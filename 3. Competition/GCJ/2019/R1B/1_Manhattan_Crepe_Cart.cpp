// Manhattan Crepe Cart

/*

- Given a 2D grid, and locations of P people in intersection with headings (NESW)
- If there are conflict, choose south and west (or the lowest val)

Input:
- P(number of people), Q(max possible value of x, y coordinate)
- following P lines:
    - Xi, Yi, Di(direction)

Limits:
T: 1-100
P: 1-500
Q = 10^5
Xi, Yi: 1-Q

if Xi=0, D != W (and so on)

*/

// my solution
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <math.h> 

using namespace std;

void printv(vector<int> seq) {
    cout << "printing seq " << endl;
    for (int i = 0; i < seq.size(); ++i) {
        cout << seq[i] << " ";
    }
    cout << endl;
}

int main()
{
	int T, n;
	T = 1;
	
	std::cin >> n;

	while (T <= n)
	{

		int P, Q;
        cin >> P >> Q;

        vector<int> VX(Q+1, 0);
        vector<int> VY(Q+1, 0);
        int maxX = 0;
        int maxY = 0;

        // allocate the remaining
        while (P--)
        {
            int X, Y;
            char C;

            std::cin >> X >> Y >> C;

            if (C == 'S') {
                for (int i = 0; i < Y; ++i) {
                    VY[i]++;
                    maxY = max(maxY, VY[i]);
                }
            } else if (C == 'N') {
                for (int i = Y+1; i <= Q; ++i) {
                    VY[i]++;
                    maxY = max(maxY, VY[i]);
                }
            } else if (C == 'W') {
                for (int i = 0; i < X; ++i) {
                    VX[i]++;
                    maxX = max(maxX, VX[i]);
                }
            } else if (C == 'E') {
                for (int i = X+1; i <= Q; ++i) {
                    VX[i]++;
                    maxX = max(maxX, VX[i]);
                }
            }
        }

        int sx, sy;

        for (int i = 0; i <= Q; ++i) {
            if (VX[i] == maxX) {
                sx = i;
                break;
            }
        }

        for (int i = 0; i <= Q; ++i) {
            if (VY[i] == maxY) {
                sy = i;
                break;
            }
        }

		std::cout << "Case #" << std::to_string(T) << ": " << sx << " " << sy << '\n';
		T++;
	}
	
	return 0;
}