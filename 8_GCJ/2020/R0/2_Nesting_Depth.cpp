// Saving The Universe Again

/*
Problem link:
https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231
*/

// my solution
#include <iostream>
#include <string>

using namespace std;

int main()
{
	int T, n;
	T = 1;
	
	std::cin >> n;

	while (T <= n)
	{
		string N, res = "";
        std::cin >> N;
		int level = 0;
		
		for (auto c : N) {
			int a = c - '0';

			while (level < a) {
				res += "(";
				++level;
			}

			while (level > a) {
				res += ")";
				--level;
			}

			res += c;
		}

		while (level > 0) {
			res += ")";
			--level;
		}

		cout << "Case #" << to_string(T++) << ": " << res << '\n';
	}
	
	return 0;
}

/* Note:
- match
*/