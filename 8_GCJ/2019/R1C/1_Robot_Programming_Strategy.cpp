// Robot Programming Strategy

/*

*/

// my solution
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

void process(vector<string>& C, char c) {
	for (auto& s : C) {
		if (s == "")
			continue;

		if (c == 'R' && s[0] == 'S') {
			s = "";
		} else if (c == 'P' && s[0] == 'R') {
			s = "";
		} else if (c == 'S' && s[0] == 'P') {
			s = "";
		} else {
			s += s[0];
			s.erase(0, 1);
		}
	}
}

int main()
{
	int T, n;
	T = 1;
	
	std::cin >> n;
	
	while (T <= n)
	{
		int N;        
        std::cin >> N;

		vector< string > C;

		for (int i = 0; i < N; ++i) {
			string a;
			std::cin >> a;
			C.push_back(a);
		}

		bool flag = true;
		vector<bool> rps(3, false);
		string res = "";

		while (flag) {
			rps[0] = rps[1] = rps[2] = false;

			for (auto& c : C) {

				if (c == "")
					continue;

				if (c[0] =='R') {
					rps[0] = true;
				} else if (c[0] =='P') {
					rps[1] = true;
				} else {
					rps[2] = true;
				}

			}

			if (!rps[0] && !rps[1] && !rps[2]) {
				flag = false;
				break;
			}

			if (rps[0] && rps[1] && rps[2]) {
				flag = false;
				res = "IMPOSSIBLE";
				break;
			}

			if (rps[0] && rps[1]) {
				res += "P";
				process(C, 'P');
				continue;
			}

			if (rps[1] && rps[2]) {
				res += "S";
				process(C, 'S');
				continue;
			}

			if (rps[0] && rps[2]) {
				res += "R";
				process(C, 'R');
				continue;
			}

			if (rps[0]) {
				res += "P";
				break;
			}

			if (rps[1]) {
				res += "S";
				break;
			}

			if (rps[2]) {
				res += "R";
				break;
			}
		}

		cout << "Case #" << to_string(T++) << ": " << res << '\n';
	}
	
	return 0;
}
