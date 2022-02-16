//Square Dance - Solution
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
        int R, C;
        cin >> R >> C;

        vector< vector<long long> > M(R, vector<long long>(C));

        // init val
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                cin >> M[i][j];
            }
        }

        vector<vector<int>> when(R, vector<int>(C, -1)); // saves when (which round) the cell is eliminated
        vector<vector<int>> up(R, vector<int>(C));
        vector<vector<int>> down(R, vector<int>(C));
        vector<vector<int>> left(R, vector<int>(C));
        vector<vector<int>> right(R, vector<int>(C));
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                up[i][j] = i - 1;
                down[i][j] = i + 1;
                left[i][j] = j - 1;
                right[i][j] = j + 1;
            }
        }

        auto GetNeighbor = [&](pair<int, int> p, int dir) {
            if (dir == 0) return make_pair(up[p.first][p.second], p.second);
            if (dir == 1) return make_pair(down[p.first][p.second], p.second);
            if (dir == 2) return make_pair(p.first, left[p.first][p.second]);
            
            return make_pair(p.first, right[p.first][p.second]);
        };

        long long total = 0;
        vector<pair<int, int>> check;

        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                total += M[i][j];
                check.emplace_back(i, j); // to be checked list
            }
        }

        long long ans = total;
        for (int iter = 0; ; iter++) {
            vector<pair<int, int>> rm; // to be removed list
            
            for (auto& p : check) {
                int sum = 0;
                int cnt = 0;
                
                for (int dir = 0; dir < 4; dir++) {
                    auto q = GetNeighbor(p, dir);
                    int qi = q.first;
                    int qj = q.second;
                    
                    if (qi >= 0 && qj >= 0 && qi < R && qj < C) {
                        sum += M[qi][qj];
                        cnt += 1;
                    }
                }

                if (sum > M[p.first][p.second] * cnt) {
                    rm.push_back(p);
                }
            }
            
            // break if nothing can be removed
            if (rm.empty()) {
                break;
            }

            for (auto& p : rm) {
                when[p.first][p.second] = iter;
                total -= M[p.first][p.second];
            }
                
            ans += total;
            vector<pair<int, int>> new_check; // to be searched list

            for (auto& p : rm) {
                for (int dir = 0; dir < 4; dir++) {
                    auto q = GetNeighbor(p, dir);
                    int qi = q.first;
                    int qj = q.second;
                    if (qi >= 0 && qj >= 0 && qi < R && qj < C) {
                        if (when[qi][qj] != iter) {
                            new_check.emplace_back(qi, qj); // add neighbors to search list (based on cell check)
                            when[qi][qj] = iter;
                        }
                    }
                }
            }
                    

            for (auto& p : rm) {
                int i = p.first;
                int j = p.second;

                if (up[i][j] != -1) {
                    down[up[i][j]][j] = down[i][j];
                }
                if (down[i][j] != R) {
                    up[down[i][j]][j] = up[i][j];
                }
                if (left[i][j] != -1) {
                    right[i][left[i][j]] = right[i][j];
                }
                if (right[i][j] != C) {
                    left[i][right[i][j]] = left[i][j];
                }
            }

            swap(check, new_check);
        }

        cout << "Case #" << to_string(T++) << ": " << ans << '\n';
        
    }
    
    return 0;
}