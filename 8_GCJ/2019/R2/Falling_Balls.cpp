// Falling Balls

/*
Link: 
https://codejam.withgoogle.com/2018/challenges/0000000000007706/dashboard

Note:
- grid of 2 or more columns
- grid of 1 or more rows
- each cell is either /, \, or empty
- leftmost and rightmost are empty, bottom row is also empty
- balls drop to top row and fall vertically, slide on ramps
- prevent balls from getting stuck at \/
- user drops ball on each column, balls do not interfere each other
- cell can contain multiple balls

Ball movement:
- move immediate below, does not move anymore on bottom row
- ball on cell \ moves below right
- ball on cell / moves below left

Input:
- C columns and x rows
- dropped balls from top and have bottom result
- create a layout that is consistent with result and uses as few rows as possible
- or if no such layout exist

Output:
- ....
- IMPOSSIBLE

EX: [3 0 0 2 0 1]
.//\..
./\./.
......

EX2: [2 0 0 3 0]
./\./

EX3. [3 0 2 0 0]
.////
././.
.....

NOTE:
- check if ball counts equals the length (always correct if so)
- longest distance ball has to travel is the row

Limit:
T: 1~100
0 <= Bi <= Ci
C: 2~100 (max 100 rows)
*/

// my solution
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

// global variables

int main()
{
	int T, n;
	T = 1;
	
	cin >> n;

	while (T <= n)
	{
		int N;
		cin >> N;

		vector<int> arr(N, 1); // top init array
		vector<int> bot_arr(N, 0); // bottom result array
		int nw = N;
		int sum = 0;

	    for (int i = 0; i < N; i++) {
		    int num;
			cin >> num;
			sum += num;
			bot_arr[i] = num;
		}
		
		if (sum != N) {
			cout << "Case #" << to_string(T) << ": " << "IMPOSSIBLE" << '\n'; 
	    	T++;
	    	continue;
		}

        vector<int> loc(N, -1);
        int run_sum = 0;
        int i = 0, j = 0;
        
        while (i < N && j < N) {
            while (bot_arr[j] > 0) {
                if (arr[i] > 0) {
                    bot_arr[j] -= arr[i];
                    loc[i] = j;
                    i++;
                }
            }
            j++;
        }
        
        if (loc[0] != 0 || loc[N-1] != N-1) {
			cout << "Case #" << to_string(T) << ": " << "IMPOSSIBLE" << '\n';
	    	T++;
	    	continue;
		}
		
		// run until it is aligned
		bool flag_change = true;
        string str = "";
        int count = 0;
		while (flag_change) {
		    
		    flag_change = false;
		    vector<int> new_loc(N, -1);

		    for (int k = 0; k < N; k++) {
    			if (loc[k] == k || loc[k] == -1) {
    			    str += '.';
    			    new_loc[k] = -1;
    			} else if (loc[k] < k) {
    			    str += (char)47; // /
    			    new_loc[k-1] = loc[k];
    			    flag_change = true;
    			} else {
    			    str += (char)92; // other
    			    new_loc[k+1] = loc[k];
    			    flag_change = true;
    			}
		    }
		    for (int k = 0; k < N; k++) {
		        loc[k] = new_loc[k];
		    }
		    str += '\n';
		    count++;
		}
	    cout << "Case #" << to_string(T) << ": " << count << '\n' << str; 
	    T++;
	}
	
	return 0;
}