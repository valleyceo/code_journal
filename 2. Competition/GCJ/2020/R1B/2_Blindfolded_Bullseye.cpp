// Blindfolded Bullseye

/* how to run:
- run: g++ 4_esab.cpp -std=c++14 -pthread -O3 -o 4_esab.o
- python 4_interactive.py python 4_tester.py 0 -- ./4_esab.o

Problem:
- Given wall of size 2x10^9 tall, 2x10^9 wide
- There lies a dart board of size AxB inside the wall. 
- Dart board may touch edge of wall
- Whenever you throw a dart on the wall, you can learn if the dart is
    1. Missed
    2. Hit inside the dart board
    3. Hit center of dart board

Question:
- Given 300 tries, can you locate center of dart board?

Solution:
- divide wall into 4 quadrant, search until a point hits dart board
- binary search to find xmin, xmax of the edge point
- binary search ymin, ymax of edge point
- you can directly find center with the edge result
- dart consumption: -> max 131 darts needed
    - less than 9 points for finding quadrant
    - binary search of ~31 darts times 4 times = 124 times
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void run() {
    int x = 0, y = 0;
    string r;

    // find first hit
    for (int i = -1; i <= 1; ++i) {
        int xg = i * 500000000;

        for (int j = -1; j <= 1; ++j) {
            int yg = j * 500000000;

            cout << xg << " " << yg << endl;
            fflush(stdout);

            cin >> r;

            if (r[0] == 'C') return;

            if (r[0] == 'H') {
                x = xg;
                y = yg;
            }
        }
    }

    int xmin, xmax, ymin, ymax;
    int rs, re;

    // find upper left xmin
    rs = -1000000000, re = x;

    while(rs < re) {
        int m = rs + (re - rs) / 2;

        cout << m << " " << y << endl;
        fflush(stdout);

        cin >> r;

        if (r[0] == 'C') return;

        if (r[0] == 'H') {
            re = m;
        } else {
            rs = m + 1;
        }
    }

    xmin = rs;

    // find upper right xmax
    rs = x, re = 1000000000;

    while(rs < re){
        int m = rs + (re - rs + 1) / 2;

        cout << m << " " << y << endl;
        fflush(stdout);

        cin >> r;

        if(r[0] == 'C') return;

        if(r[0] == 'H') {
            rs = m; 
        } else {
            re = m - 1;
        }
    }

    xmax = re;

    // find upper left ymax
    rs = -1000000000, re = y;

    while (rs < re) {
        int m = rs + (re - rs) / 2;

        cout << x << " " << m << endl;
        fflush(stdout);
        
        cin >> r;

        if(r[0] == 'C') return;

        if(r[0] == 'H'){
            re = m;
        } else {
            rs = m + 1;
        }
    }

    ymin = rs;

    // find upper left ymax
    rs = y, re = 1000000000;

    while (rs < re) {
        int m = rs + (re - rs + 1) / 2;

        cout << x << " " << m << endl;
        fflush(stdout);
        
        cin >> r;

        if(r[0] == 'C') return;

        if(r[0] == 'H'){
            rs = m;
        } else {
            re = m - 1;
        }
    }

    ymax = re;

    // now you have perfect result
    cout << (xmin + xmax)/2 << " " << (ymin + ymax)/2 << endl;
    fflush(stdout);
    
    cin >> r;
}

int main() {
    int T, a, b;
    
    cin >> T >> a >> b;

    while (T--)
    {
        run();
    }

    return 0;
}