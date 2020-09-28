// Pascal Walk

/*

*/

// my solution
#include <iostream>
#include <vector>

using namespace std;

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

/* Sol1
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  cin >> tt;
  for (int qq = 1; qq <= tt; qq++) {
    cout << "Case #" << qq << ":\n";
    int n;
    cin >> n;
    int rows = min(30, n);
    n -= rows;
    vector<int> a(rows);
    for (int row = rows - 1; row >= 0; row--) {
      if (n >= (1 << row) - 1) {
        a[row] = 1;
        n -= (1 << row) - 1;
      }
    }
    rows += n;
    a.resize(rows);
    int side = 0;
    for (int row = 0; row < rows; row++) {
      if (a[row] == 1) {
        if (side == 0) {
          for (int j = 0; j <= row; j++) {
            cout << row + 1 << " " << j + 1 << '\n';
          }
        } else {
          for (int j = row; j >= 0; j--) {
            cout << row + 1 << " " << j + 1 << '\n';
          }
        }
        side ^= 1;
      } else {
        if (side == 0) {
          cout << row + 1 << " " << 1 << '\n';
        } else {
          cout << row + 1 << " " << row + 1 << '\n';
        }
      }
    }
  }
  return 0;
}
*/

/* sol2
#include<bits/stdc++.h>
using namespace std;

vector<pair<int, int>> solve(int N) {
    vector<pair<int, int>> ans;
    if (N <= 30) {
        for (int i = 0; i < N; i++) {
            ans.emplace_back(i, 0);
        }
    } else {
        N -= 30;
        int numExtra = 0;
        bool high = false;
        for (int i = 0; i < 30; i++) {
            if (N & (1 << i)) {
                if (high) {
                    for (int z = i; z >= 0; z--) {
                        ans.emplace_back(i, z);
                    }
                } else {
                    for (int z = 0; z <= i; z++) {
                        ans.emplace_back(i, z);
                    }
                }
                numExtra++;
                high = !high;
            } else {
                if (high) {
                    ans.emplace_back(i, i);
                } else {
                    ans.emplace_back(i, 0);
                }
            }
        }
        for (int i = 30; numExtra; i++) {
            if (high) {
                ans.emplace_back(i, i);
            } else {
                ans.emplace_back(i, 0);
            }
            numExtra--;
        }
    }
    return ans;
}

int main() {
    ios_base::sync_with_stdio(false), cin.tie(nullptr), cout.tie(nullptr);
    int T; cin >> T;

    for (int case_num = 1; case_num <= T; case_num ++) {
        int N; cin >> N;
        auto ans = solve(N);
        cout << "Case #" << case_num << ":" << '\n';
        for (auto it : ans) {
            cout << it.first+1 << ' ' << it.second+1 << '\n';
        }
    }

    return 0;
}


*/


/* sol 3

#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
const int maxn=1e6+7;
const int inf=INT_MAX;
const ll inff=1e18;
const ll mod=1e9+7;
#define pii pair<int,int>
#define mkp make_pair
#define F first
#define S second
#define pb push_back
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(),(v).end()
//#define int ll

#ifdef HNO2
#define IOS
#else
#define endl '\n'
#define IOS ios::sync_with_stdio(0); cin.tie(0);
#endif // HNO2

void init(int x)
{
    cout<<"Case #"<<x<<":"<<endl;
}

int32_t main()
{
    IOS
    int t;
    cin>>t;
    for (int _=1;_<=t;_++)
    {
        init(_);

        int n;
        cin>>n;
        if (n<=50)
        {
            for (int i=1;i<=n;i++) cout<<i<<' '<<1<<endl;
            continue;
        }

        int N=n-35;
        vector<int> v;
        while (N) v.pb(N&1),N>>=1;

        int sum=0;
        for (int i=0;i<sz(v);i++)
            if (v[i]==0) sum++;
            else sum+=(1<<i);

        int head=1;
        for (int i=0;i<sz(v);i++)
        {
            if (v[i]==1)
            {
                if (head)
                    for (int j=1;j<=i+1;j++) cout<<i+1<<' '<<j<<endl;
                else
                    for (int j=i+1;j>=1;j--) cout<<i+1<<' '<<j<<endl;
                head^=1;
            }
            else
            {
                if (head) cout<<i+1<<' '<<1<<endl;
                else cout<<i+1<<' '<<i+1<<endl;
            }
        }
        int now=sz(v)+1;
        for (int i=sum+1;i<=n;i++)
            if (head) cout<<now<<' '<<1<<endl,now++;
            else cout<<now<<' '<<now<<endl,now++;
    }
}



*/