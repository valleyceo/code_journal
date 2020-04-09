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
		std::string N;        
        std::cin >> N;
		
		string A = "";
		string B = "";
		int idx = 0;
		
		while (N[idx] != '4' && idx < N.length()) {
			A += N[idx];
			idx++;
		}

		while (idx < N.length()) {
			if (N[idx] == '4') {
				A += '2';
				B += '2';
			} else {
				A += N[idx];
				B += '0';
			}
			idx++;
		}
		cout << "Case #" << to_string(T++) << ": " << A << " " << B << '\n';
	}
	
	return 0;
}

/* Note:
- Someone won lottery, we owe them N coins
- Integer 4 key is broken
- Create 2 integer A, B (both positive) such that neither contains 4 and A + B = N
- Find any pair that satisfy these condition

Test case:
1: 4 => 2 2
2: 940 => 852 88
3: 4444 => 667 3777

Limitations:
Test: 1~100
Memory: 1GB
At least 1 digit of N is 4
T1: 1 < N < 10^5
T2: 1 < N < 10^9
T3: 1 < N < 10^100

My test case:
4 = 2 2
24 = 12 12
14 = 5 7
12524647345 = 12522627325 + 2020020
*/