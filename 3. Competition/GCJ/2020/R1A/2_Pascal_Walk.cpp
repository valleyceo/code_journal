// Pascal Walk

/*

*/

// my solution
#include <iostream>
#include <vector>

int DP[100][100] = {0};
bool PATH[100][100] = {0};

// Returns value of Binomial Coefficient C(n, k) 
int binomialCoeff(int n, int k) 
{
    // Caculate value of Binomial Coefficient 
    // in bottom up manner 
    for (i = max_level; i <= n; i++) 
    { 
        for (j = 0; j <= min(i, k); j++) 
        { 
            // Base Cases 
            if (j == 0 || j == i) 
                DP[i][j] = 1; 
  
            // Calculate value using previously 
            // stored values 
            else
                DP[i][j] = C[i - 1][j - 1] + C[i - 1][j]; 
        } 

        if (i < n)
            max_level = i;
    } 
  
    return DP[n][k]; 
}

int main()
{
    int T, n;
    T = 1;
    
    std::cin >> n;

    while (T <= n)
    {
        int val;
        std::cin >> val;


        int r = 1, c = 1;
        PATH[r][c] = true;
        sum = 1;
        vector< vector<int> > res;

        while (val < sum) {
            vector<int> coord;

            if (sum < val/2) {
                r += 1;
                c += 1;
                sum += binomialCoeff(int n, int k);
            } else {
                r -= 1;
                c -= 1;
                sum += 
            }
            coord.push_back({r, c});
            res.push_back(coord);
        }

        cout << "Case #" << to_string(T++) << '\n';
        for (auto v : res) {
            cout << v[0] << " " << v[1] << endl;
        }
    }
    
    return 0;
}

/* Note:

*/