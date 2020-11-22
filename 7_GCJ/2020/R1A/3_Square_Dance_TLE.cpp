//Square Dance - My ans (TLE)
#include <iostream>
#include <string>
#include <vector>

using namespace std;

struct cell {
    bool left_break = false, right_break = false;
    long long int val;
    cell *up = nullptr, *down = nullptr, *left = nullptr, *right = nullptr;
};

void PrintVec(vector< vector<cell> >& M) {
    cout << "Printing V" << endl;
    for (int i = 0; i < M.size(); ++i) {
        for (int j = 0; j < M[0].size(); ++j) {
            cout << M[i][j].val << " ";
        }
        cout << endl;
    }
}

bool check_round(cell* CellIterator) {
    double adj_count = 0.0;
    double adj_sum = 0.0;

    // check top
    if (CellIterator->up) {
        adj_count++;
        adj_sum += abs(CellIterator->up->val);
        //cout << "UP";
    }

    // check bot
    if (CellIterator->down) {
        adj_count++;
        adj_sum += abs(CellIterator->down->val);
        //cout << "Down";
    }

    // check left
    if (CellIterator->left && !CellIterator->left_break) {
        adj_count++;
        adj_sum += abs(CellIterator->left->val);
        //cout << "Left";
    }

    // check right
    if (CellIterator->right && !CellIterator->right_break) {
        adj_count++;
        adj_sum += abs(CellIterator->right->val);
        //cout << "Right";
    }

    //cout << endl;

    return (adj_sum / adj_count) > CellIterator->val;
}

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int R, C;
        cin >> R >> C;

        vector< vector<cell> > M(R, vector<cell>(C + 1));
        
        M[0][0].right = &M[0][1];
        M[0][1].left = &M[0][0];

        // init val
        for (int i = 0; i < R; ++i) {
            M[i][C].right_break = true;
            M[i][1].left_break = true;

            if (i < R - 1) {
                M[i][C].right = &M[i + 1][1];
            }

            if (i > 0) {
                M[i][1].left = &M[i-1][C];
            }

            for (int j = 1; j < C + 1; ++j) {

                int val;
                cell temp_cell;

                cin >> val;
                M[i][j].val = val;

                if (i > 0)
                    M[i][j].up = &M[i - 1][j];

                if (i < R - 1)
                    M[i][j].down = &M[i + 1][j];

                if (j > 1)
                    M[i][j].left = &M[i][j - 1];

                if (j < C)
                    M[i][j].right = &M[i][j + 1];
            }
        }

        bool has_elimination = true;
        long long int res = 0;

        while (has_elimination) {
            has_elimination = false;

            //cout << "printing" << endl;
            //PrintVec(M);

            // get sum
            long long int sum = 0;

            // search
            for (int i = 0; i < R; ++i) {
                cell* Ritr = &M[i][0];

                while (Ritr->right) {
                    Ritr = Ritr->right;
                    sum += Ritr->val;
                    
                    //cout << Ritr->val << endl;
                    //cout << Ritr->left_break << " " << Ritr->right_break << endl;

                    if (check_round(Ritr)) {
                        has_elimination = true;
                        Ritr->val = -Ritr->val;
                    }
                }
            }

            // eliminate
            if (has_elimination) {
                cell* Ritr = &M[0][0];

                while (Ritr->right) {
                    Ritr = Ritr->right;

                    if (Ritr->val < 0) {
                        Ritr->val = 0;

                        if (Ritr->up && Ritr->down) {
                            Ritr->up->down = Ritr->down;
                            Ritr->down->up = Ritr->up;                                
                        } else {
                            if (Ritr->up) {
                                Ritr->up->down = nullptr;
                            }

                            if (Ritr->down) {
                                Ritr->down->up = nullptr;
                            }
                        }

                        if (Ritr->left && Ritr->right) {
                            Ritr->left->right = Ritr->right;
                            Ritr->right->left = Ritr->left;

                            if (Ritr->right_break){
                                Ritr->left->right_break = true;
                            }

                            if (Ritr->left_break) {
                                Ritr->right->left_break = true;
                            }
                        } else {
                            if (Ritr->left) {
                                Ritr->left->right = nullptr;
                            }

                            if (Ritr->right) {
                                Ritr->right->left = nullptr;
                            }
                        }
                    }
                }
            }
            
            res += sum;
        }

        cout << "Case #" << to_string(T++) << ": " << res  << '\n';
        
    }
    
    return 0;
}

/* Note:
- R row C col grid
- R x C competitors
- Each competitor occupies one square unit cell, stays until elminated
- Compass neighbor: shares same row or col, and there is no val in btw (may have btw 0 to 4)
- if competitor had at least 1 compass neighbor, and if its level is less than average of neighbors, it is eliminated (elimination happens after the round)
- competition ends if there are no more elimination
- Interest level = sum of all skill levels in that round
- interest level of competition = sum of all interest level of all round

- given grid, what is interest level of competition?
*/