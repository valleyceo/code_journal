#include <iostream>
#include <string>
#include <vector>
#include <bitset>

using namespace std;

int main() {
    int num_test_cases;
    cin >> num_test_cases;

    for (int t = 0; t < num_test_cases; ++t) {
      int n, b, f;
      cin >> n >> b >> f;
      string res = "", s_ans;

      // create guess matrix
      vector<vector<char> > M(5);
      for (int i = 0; i < 5 ; i++) {
        M[i].resize(n);
      }

      vector<vector<char> > M_RES(5);
      for (int i = 0; i < 5 ; i++) {
        M_RES[i].resize(n-b);
      }

      int val = 1;

      for (int i = 0; i < n; ++i) {
          bitset<5> bin_x(val);
          string x = bin_x.to_string();
          
          for (int j = 0; j < 5; ++j) {
              M[j][i] = x[j];
          }

          val++;
          if (val == 32) {
              val = 1;
          }
      }

      // interact
      for (int i = 0; i < 5; ++i) {
        string s = "";
        for (int j = 0; j < n; ++j) {
          s += M[i][j];
        }

        cout << s << endl;
        cin >> s_ans;

        for (int k = 0; k < n-b; ++k) {
          M_RES[i][k] = s_ans[k];
        }
      }

      int r_idx = 0;
      int b_count = 0;

      // find solution
      for (int i = 0; i < n; ++i) {
        bool match = true;
        for (int j = 0; j < 5; ++j) {
          if (M[j][i] != M_RES[j][r_idx]) {
            res += to_string(i) + ' ';
            match = false;
            b_count++;
            break;
          }
        }

        if (match) {
          r_idx++;
        }

        if (b_count == b) {
          break;
        }
      }

      // found anser
      res.pop_back();
      cout << res;
    }
    return 0;
}