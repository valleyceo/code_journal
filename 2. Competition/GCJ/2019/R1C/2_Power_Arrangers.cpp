// Lollipop Shop

/*
Link:
https://codejam.withgoogle.com/2018/challenges/0000000000007765/dashboard/000000000003e068

Note:"
- make N lollipops per day
- flavor: hb, cherry, lime (each unique)
- N customers come, one at time
- gives you list of flavors they like
- if none flavor exist, you cannot sell
- preference of flavor by chance, non-uniform distribution
- each flavor has x% chance of being liked
- values are chosen independently and uniformly at random (0.005 ~ 0.1)
- required to sell a number of lollipops that is at least 90% of M for each input case

Input:
- T: # of test cases
- N: # of lollipops (# of customers)
- D (ID of flavors in increasing order)
- (#D integers) id1, id2,... idn (integer, range 0~N-1, 0 for some or all customers)

*/

// run: g++ q3.cpp -std=c++14 -pthread -O3 -o q3.out
// python testing_tool.py ./q3.out
// my solution
#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;

// global variables
int tries, N, L;

int main()
{
	int T, n;
	T = 1;
	
	cin >> n;

	while (T <= n)
	{
		cin >> N; // flavors or customers
		
		int nf; // number of flavors a custumer likes
		int choice; // find an available flavor
		int wanted; // currently wanted flavor
		vector<bool> sold(N, false);
		vector<int> dist(N, 0);

		for (int i = 0; i < N; i++) {
			cin >> nf;
			choice = -1;

			// go over customer's wanted flavors
			for (int j = 0; j < nf; j++) {
				cin >> wanted;
				dist[wanted]++;
				// pick unsold and less popular option
				if (!sold[wanted] && (choice==-1 || dist[wanted] < dist[choice]) ) {
					choice = wanted;
				}
			}

			// check sold array
			if (choice >= 0)
				sold[choice] = true;

			cout << choice << endl;
		}
		T++;
	}
	
	return 0;
}
