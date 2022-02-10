// Lollipop Shop

/*
Run:
g++ 2_Lollipop_Shop.cpp -std=c++14 -pthread -O3 -o 2_Lollipop_Shop.o
python testing_tool.py ./2_Lollipop_Shop.o

Problem:
- N lollipops with each unique flavor
- N customers come with preference (like/dislike) of each flavor
- if none flavor exist, you cannot sell
- preference of flavor by chance, non-uniform distribution
- each flavor has x% chance of being liked
- values are chosen independently and uniformly at random (0.005 ~ 0.1)
- required to sell a number of lollipops that is at least 90% of M for each input case

Question:
- Sell as many lollipops as possible

Input:
- T: # of test cases
- N: # of lollipops (# of customers)
- D (ID of flavors in increasing order)
- (#D integers) id1, id2,... idn (integer, range 0~N-1, 0 for some or all customers)
*/


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
