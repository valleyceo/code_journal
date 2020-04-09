// Ant Stack

/*
Link:
https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e0a8

Note:
- N ants
- each ant has L, W
- place food at top of ant farm
- ants will stack vertically
- each ant stack directly holding the next on its back
- ants are able to carry up to 6 times their own weight(ex. 8mg can carry 48mg)
- all ants have different body length

Requirements:
- stack must be linear
- each ant must be direcly below exactly one ant
- length of ants must be strictly decreasing from bottom to top
- sum of weights of all ants above must be no more than 6 times weight

Question:
- what is the max number these ants can stack?

Input:
- T test case
- N # of ants
- (#N lines) W1, W2,... Wn (Wi is weight of i'th ant, length strictly increasing order)

Limits:
- T (7~100)
- N (2~1e5)
- W (1~1e9)

Example:
2
9 1 
Ans: 1

*/

// my solution
#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int main()
{
	int T, n;
	T = 1;
	
	cin >> n;

	while (T <= n)
	{
	    int N;
		cin >> N;
		
		vector<int> ants(N, 0);
        vector<long long> dp(N, 0);
        
        // get ant weights in reverse order
        for (int i = 0; i < N; i++) {
            int w;
            cin >> w;
            ants[N-i-1] = w;
        }
		
		int best = 0;
		dp[0] = LLONG_MAX; // start with max val dp

		// loop from bottom ant
		for (int i = 0; i < N; i++) {
		    // check dp backwards (for better maxweight)
		    for (int j = best; j >= max(0, best-(N-i)-1); j--) {
		        if (dp[j] >= ants[i]) {
		        	// maximize next dp from minimum next weight
		            dp[j+1] = max(dp[j+1], min(dp[j]-ants[i], ants[i]*6LL) ); // convert LL
		            best = max(best, j + 1);
		        }
		    }
		}
		
		cout << "Case #" << to_string(T) << ": " << best << '\n'; 
		T++;
	}
	
	return 0;
}

//source: https://github.com/ruippeixotog/google-code-jam-2018/blob/master/round1c/ant-stack.cpp