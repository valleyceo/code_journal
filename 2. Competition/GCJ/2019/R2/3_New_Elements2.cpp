// Graceful Chainsaw Jugglers

/*
Link:
https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e068

Note:
- Unlimited # of jugglers
- each know how to juggle any # of chainsaw
- choose # of jugglers, distribute red and blue chainsaws
- each juggler gets at least one chainsaw
- each chainsaw used only once
- audience happy when many jugglers and chainsaw used as possible
- jugglers cannot use same # of R or B

Input:
- T
- R, B (number of R, B chainsaw)

Output:
- x: largest number of jugglers you can use

Limits:
- T (1~100)
- R + B > 0
- R,B(1~50)

Ex.
1 - 2R 3B
2 - 1R

Note:
basic (1 0), (0 1), (2 0), (0 2), (2 1), (1 2), (2 2)... does not work 
counter case:
10, 10 -> turn: (2 2), left: (3 3) -> better case: (3 0), (0 3)
*/
#include <iostream>
#include <string>
#include <vector>

using namespace std;

// global variables

int main()
{
	int T, n;
	T = 1;
	
	cin >> n;

	// solve dp first
	int dp_size = 500;
	vector<vector<int>> dp(dp_size+1, vector<int>(dp_size+1, 0));
	bool flag_stop;
	int i, j, k, l;
	for (i = 0; i < dp_size; i++) {
		for (j = 0; j < dp_size; j++) {
		    if (i == 0 && j == 0) continue;
		    
			flag_stop = true;

			for (k = dp_size; k >= i; k--) {
				for (l = dp_size; l >= j; l--) {
					if (dp[k][l] <= dp[k - i][l - j]) {
						dp[k][l] = dp[k - i][l - j] + 1;
						flag_stop = false;
					}
				}
			}
			
			if (flag_stop) break;
		}
		
		if (j == 0) break;
	}
    
	while (T <= n)
	{
		int R, B;
		cin >> R >> B;

	    cout << "Case #" << to_string(T) << ": " << dp[R][B] << '\n'; 
	    T++;
	}
	
	return 0;
}

// link: https://codejam.withgoogle.com/2018/challenges/0000000000007706/attempts/for/cubelover