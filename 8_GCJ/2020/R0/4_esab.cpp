// ESAb Interactive

/* how to run:
- run: g++ 4_esab.cpp -std=c++14 -pthread -O3 -o 4_esab.o
- python 4_interactive.py python 4_tester.py 0 -- ./4_esab.o
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void PrintVec(vector<int> V) {
    string s = "";
    for (auto v : V) {
        s += to_string(v) + " ";
    }
    cout << s << endl;
}

int main() {
    int T, blen;
    
    cin >> T >> blen;
    vector<int> BV(blen, 0);

    while (T--)
    {
        int diff_idx = -1, same_idx = -1;
        int diff_prev, same_prev;
        int idx = 0;
        int in_count = 0;
        string res = "";
        string result;

        while (idx < blen / 2) {
            int l, r;
            
            cout << idx + 1 << endl;
            fflush(stdout);

            cin >> l;
            BV[idx] = l;

            cout << blen - idx << endl;
            fflush(stdout);

            cin >> r;
            BV[blen - idx - 1] = r;

            if (same_idx < 0 && l == r) {
                same_idx = idx;
                same_prev = l;
            }

            if (diff_idx < 0 && l != r) {
                diff_idx = idx;
                diff_prev = l;
            }

            in_count += 2;
            in_count %= 10;

            if (in_count == 0) {
                int diff_new, same_new;

                // get prev vals
                if (diff_idx < 0) {
                    cout << 1 << endl;
                } else {
                    cout << diff_idx + 1 << endl;
                }
                fflush(stdout);
                cin >> diff_new;

                if (same_idx < 0) {
                    cout << 1 << endl;
                } else {
                    cout << same_idx + 1 << endl;
                }
                fflush(stdout);
                cin >> same_new;

                //cout << "sameNew: " << same_new << endl;
                //cout << "diffNew: " << diff_new << endl;
                if (same_idx > -1 && same_prev != same_new) {
                    //cout << "change same" << endl;

                    for (int j = 0; j <= idx; ++j) {
                        BV[j] ^= 1;
                    }

                    for (int j = blen -1 - idx; j < blen; ++j)
                        BV[j] ^= 1;
                } 

                if (diff_idx > -1 && same_idx > -1 && 
                    ((diff_prev != diff_new && same_prev == same_new) || 
                     (diff_prev == diff_new && same_prev != same_new))) {
                    //cout << "change diff" << endl;
                    reverse(BV.begin(), BV.end());
                } else if (diff_idx > -1 && same_idx == -1 && diff_prev != diff_new) {
                    reverse(BV.begin(), BV.end());
                } 

                same_prev = same_new;
                diff_prev = diff_new;
                
                in_count += 2;
                in_count %= 10;
            }

            ++idx;
        }

        res = "";
        for (int i = 0; i < blen; ++i) {
            res += to_string(BV[i]);
        }

        cout << res << endl;
        fflush(stdout);

        cin >> result;
        if (result[0] == 'N')
            break;
    }

    return 0;
}

/*
Note:
Test inputs
example: 1100011010

1 10 // T, b
1
0  //first diff (idx : 0)
1
1  // first same (idx: 1)
1 //get current diff
1 //get current same
1
0
1
1
0 // changed diff -> now 0101100011
1 // changed same
0
0
1
0
1
0

<INPUT>
1 10
1
0
1
1
1
1
1
0
1
1
0
1
0
0
1
0
1
0

example 1101100011
1 10
1
1 // first same(0)
1
1
0
0
1
0 //first diff(3)
1 //consume 8(1)
1 //consume 8(1) -> flip
1 // SET diff
1 // SET same
1
1
1
1
0
0
1
0
0 //diff changed - 1100011011
0 //same changed -> 0011100100
1
0

<INPUT>
1 10
1
1
1
1
0
0
1
0
1
1
1
1
1
1
1
1
0
0
1
0
0
0
1
0

EXAMPLE: 1100000101
1 10
1
1 first same(0)
1
0 first diff(1)
1 curr diff
1 curr same
1
1
1
0
0 diff changed -> 1010000011
0 same changed -> 0101111100
0
1
1
1
1
1

<input>
1 10
1
1
1
0
1
1
1
1
1
0
0
0
0
1
1
1
1
1

EXAMPLE: 1111100000
1 10
1
1 first dif(0)
1
1
1
1
1
1
1 idx = 10
1 get first idx

<input>
1 10
1
1
1
1
1
1
1
1
1
1
*/