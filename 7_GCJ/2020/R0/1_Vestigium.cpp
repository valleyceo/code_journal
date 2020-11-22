// Saving The Universe Again

/*
Problem link:
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
*/

// my solution
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

int main()
{
	int T, n;
	T = 1;
	
	std::cin >> n;
	
	while (T <= n)
	{
		int N;        
        std::cin >> N;
		int k = 0, r = 0, c = 0;

		vector<vector<int> >M;
		int a;

		for (int i = 0; i < N; ++i) {
			unordered_set<int> uset;
			vector<int> temp;

			for (int j = 0; j < N; ++j) {
				std::cin >> a;
				temp.push_back(a);

				if (i == j) {
					k += a;
				}
			}
			M.push_back(temp);
		}

		unordered_set<int> uset_row, uset_col;

		for (int i = 0; i < N; ++i) {
			uset_row.clear();
			uset_col.clear();

			for (int j = 0; j < N; ++j) {
				if (uset_row.find(M[i][j]) != uset_row.end()) {
					++r;
					break;
				} else {
					uset_row.insert(M[i][j]);
				}
			}

			for (int j = 0; j < N; ++j) {
				if (uset_col.find(M[j][i]) != uset_col.end()) {
					++c;
					break;
				} else {
					uset_col.insert(M[j][i]);
				}
			}
		}

		cout << "Case #" << to_string(T++) << ": " << k << " " << r << " " << c << '\n';
	}
	
	return 0;
}

/* Note:
- k: trace
- r: number of rows with duplicate
- c: number of cols with
*/