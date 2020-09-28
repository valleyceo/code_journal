// Draupnir (Interactive problem)

/*
Question summary:
- Ring that copies themselves
- Each X-day ring produce one more X-day ring every X-day
- Possible rings are 1~6-day ring
- at day 0, you have Ri of i-day rings (R=1~100, i=1~6)
- you can find todal number of rings on day x (x=1-500)
- total ans return is modulo 2^63
- you can check W times

Solution
*/

//https://github.com/ruippeixotog/google-code-jam-2018/blob/master/round1a/bit-party.cpp
#include <iostream>
#include <algorithm>    // std::sort
#include <vector>
#include <cmath>
#include <queue>
#include <map>
#include <set>

using namespace std;

bool is_contiguous(set<int> seq) {
    int i = -1;
    for (auto a : seq) {
        if (i == -1) {
            i = a;
        } else {
            if (i+1 == a) {
                i = a;
            } else {
                return false;
            }
        }
    }
    
    return true;
}

int main()
{
    int T, n;
    long long mtime;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int signs;
        std::cin >> signs;

        long long int D, A, B;

        map<long long int, set<int>> M_MAP;
        map<long long int, set<int>> N_MAP;
        
        for (int i = 0; i < signs; i++) {
            std::cin >> D >> A >> B;
            M_MAP[D + A].insert(i);
            N_MAP[D - B].insert(i);
        }

        std::map<long long int, set<int>>::iterator it_m;
        std::map<long long int, set<int>>::iterator it_n;
        
        int max_size = -1;
        set<int> new_set;
        set<set<int>> valid_sets;
        
        for (it_m = M_MAP.begin(); it_m != M_MAP.end(); it_m++) {
            for (it_n = N_MAP.begin(); it_n != N_MAP.end(); it_n++) {
                new_set.clear();
                new_set.insert(it_m->second.begin(), it_m->second.end());
                new_set.insert(it_n->second.begin(), it_n->second.end());
                
                // check if set is contiguous
                if(!is_contiguous(new_set)) {
                    continue;
                }
                
                if ((int)new_set.size() > max_size) {
                    max_size = (int)new_set.size();
                    valid_sets.clear();
                    valid_sets.insert(new_set);
                    
                } else if ((int)new_set.size() == max_size) {
                    if (valid_sets.find(new_set) != valid_sets.end()) {
                        continue;
                    } else {
                        valid_sets.insert(new_set);
                    }
                }
            }
        }

        printf("Case #%d: %d %d\n", T, max_size, (int)valid_sets.size());
        T++;
    }
    
    return 0;
}