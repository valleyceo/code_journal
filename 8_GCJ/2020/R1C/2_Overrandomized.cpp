// Overrandomized

/*
Problem:
- Random number generator
- Request positive integer M (up to U decimal digit)
- Respond with integer from 1-M inclusive
- Use random subset of 10 distinct letters
- Random mapping of the letter and 0-9

Question:
- Find the digit string

*/
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
#include <unordered_map>
#include <set>
#include <algorithm>

using namespace std;

char maxFromRange(const vector< pair<string, int> >& PV, int rs) {
    
    int maxv = -1;
    char mchar;
    vector<int> dp(26, 0);

    for (int i = rs; i < rs + 10; ++i) {
        string temp = PV[i].first;
        dp[temp[0] - 'A']++;
    }

    for (int i = 0; i < 26; ++i) {
        if (dp[i] > maxv) {
            maxv = dp[i];
            mchar = 'A' + i;
        }
    }

    return mchar;
}

bool comp(pair<string, int> a, pair<string, int> b) {
    return a.second > b.second;
}

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int U;
        cin >> U;

        int X = 10000;
        vector<int> M(99);
        vector<int> M2(110);
        unordered_map<string, int> umap;
        set<char>SS;

        while (X--) {
            int num;
            string letter;
            cin >> num >> letter;

            M[num]++;
            umap[letter]++;

            for (auto c : letter) {
                SS.insert(c);
            }
        }
        
        vector< pair<string, int> > PV(umap.begin(), umap.end());
        sort(PV.begin(), PV.end(), comp);

        string one2three = PV[0].first + PV[1].first + PV[2].first +PV[3].first;
        string four2nine = "";
        string zero = "";

        cout << PV.size() << endl;

        for (int rg = 50; rg <= 90; rg += 10) {
            int maxv = -1;
            char mchar = '-';
            vector<int> dp(26, 0);

            for (int i = rg; i < min(rg + 10, (int)PV.size()); ++i) {
                string temp = PV[i].first;
                dp[temp[0] - 'A']++;
            }

            for (int i = 0; i < 26; ++i) {
                if (dp[i] > maxv) {
                    maxv = dp[i];
                    mchar = 'A' + i;
                }
            }

            four2nine += mchar;
        }

        string one2nine = one2three + four2nine;

        // find 0
        for (auto c : one2nine) {
            SS.erase(c);
        }

        for (auto s : SS) {
            zero += s;
        }

        string res = zero + one2three + four2nine;

        cout << "Case #" << to_string(T++) << ": " << res << '\n';
    }
    
    return 0;
}