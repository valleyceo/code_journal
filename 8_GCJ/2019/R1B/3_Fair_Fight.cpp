// Transmutation

/*

- Given a rack of N array of int
- Pick a pair of integers (L, R) where 1 <= L <= R <= N
- Duellers have Ci, Di skill level
- It is possible to chose the same type (multiples of each)
- Keep the absolute skill level difference to K
- 0 does not count

- Find the number of choices you can make that result in fair fight

Input: 
- N(number of rack), K (abs diff)
- First line is Charles' skill
- Second line is Delila's skill

-> 
Create sorted hash count
loop through and find the intersection
*/

// my solution

// my solution
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <math.h> 
#include <map>
#include <queue>

using namespace std;

void printM(map<int, int> m) {
	map<int, int>::iterator it;

	cout << "printing seq " << endl;
	for (it = m.begin(); it != m.end(); it++) {
        cout << it->first << "(" << it->second << ") ->";
    }
    cout << endl;
}

int getMax(vector<int> v) {
	int m = v[0];
	if (v.size() == 1)
		return;

	for (int i = 1; i < v.size(); ++i) {
		m = max(m, v[i]);
	}
	return m;
}

int main()
{
	int T, n;
	T = 1;
	
	std::cin >> n;

	while (T <= n)
	{

		int N, K, num;
        cin >> N >> K;
        cout << N << " " << K << endl;
        map<int, vector<int>> mapC, mapD;
        vector<int> vecC(N, 0);
        vector<int> vecD(N, 0);
        vector<bool> bmap(N, true);

        for (int i = 0; i < N; ++i) {
        	cin >> num;
        	mapC[num].push(i);
        	vecC[i] = num;
        }

        for (int i = 0; i < N; ++i) {
        	cin >> num;
        	mapD[num].push(i);
        	vecD[i] = num;
        }

        int i1 = 0, j1 = 0;

        maxC = getMax(vecC);
        maxD = getMax(vecD);

        while (abs(maxC - maxD) < K)) {
			if (maxC > maxD) {
				for (auto x : mapC[maxC]) {
					bmap[x] = false;
				}
			} else {
				for (auto x : mapD[maxD]) {
					bmap[x] = false;
				}
			}

			maxC = getMax(vecC);
        	maxD = getMax(vecD);
		}

        int res = 0;

        for (itC = mapC.begin(); itC != mapC.end(); itC++) {
        	for (itD = mapD.begin(); itD != mapD.end(); itD++) {
        		if (abs(itC->first - itD->first) <= K) {
        			res += min(itC->second, itD->second);
        		}
        	}
        }


		std::cout << "Case #" << std::to_string(T) << ": " << res << '\n';
		T++;
	}
	
	return 0;
}