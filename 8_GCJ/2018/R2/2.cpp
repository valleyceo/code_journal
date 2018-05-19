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

*/
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
		int R, B;
		cin >> R >> B;

	    int lv = 1;
	    int ct = 0;
	    bool change_flag = true;

	    while (change_flag) {
	    	change_flag = false;
            
            for (int i = 0; i < lv; i++) {
                if (R >= lv && B >= i) {
    	    		R -= lv;
    	    		B -= i;
    	    		ct++;
    	    		change_flag = true;
    	    	}
    	    	
    	    	if (B >= lv && R >= i) {
    	            R -= i;
    	            B -= lv;
    	    		ct++;
    	    		change_flag = true;
    	    	}
            }
	    	

	    	if (R >= lv && B >= lv ) {
	    		R -= lv;
	    		B -= lv;
	    		ct++;
	    		change_flag = true;
	    	}
	    	
	    	lv++;
	    }

	    cout << "Case #" << to_string(T) << ": " << ct << '\n'; 
	    T++;
	}
	
	return 0;
}

// link: https://codejam.withgoogle.com/2018/challenges/0000000000007706/attempts/for/cubelover
// solution
#include <cstdio>
#include <algorithm>
#include <iostream>

using namespace std;

int d[505][505];
int dsize = 20;

int main() {
	int i, j, k, l;
	for (i = 0;; i++) {
		for (j = 0;; j++) if (i || j) {
			int t = 1;
			for (k = dsize; k >= i; k--) {
			    for (l = dsize; l >= j; l--) {
    				if (d[k][l] <= d[k - i][l - j]) {
    					d[k][l] = d[k - i][l - j] + 1;
    					t = 0;
    				}
			    }
			}
			if (t) break;
		}
		if (j == 0) break;
	}
	
	for (int a = 0; a <= dsize; a++) {
	    for (int b = 0; b <= dsize; b++) {
	        cout << d[a][b] << " ";
	    }
	    cout << endl;
	}
	cout<<endl;
                	
	int T, Tn;
	scanf("%d", &Tn);
	for (T = 1; T <= Tn; T++) {
		scanf("%d%d", &i, &j);
		printf("Case #%d: %d\n", T, d[i][j]);
	}
}


0 1 1 2 2 2 3 3 3 3 4 4 4 4 4 5 5 5 5 5 5 
1 2 2 3 3 3 4 4 4 4 5 5 5 5 5 6 6 6 6 6 6 
1 2 3 3 4 4 4 5 5 5 5 6 6 6 6 6 7 7 7 7 7 
2 3 3 4 4 4 5 5 5 6 6 6 6 7 7 7 7 7 8 8 8 
2 3 4 4 5 5 5 6 6 6 6 7 7 7 7 7 8 8 8 8 8 
2 3 4 4 5 5 6 6 6 7 7 7 7 8 8 8 8 8 9 9 9 
3 4 4 5 5 6 6 6 7 7 7 7 8 8 8 8 9 9 9 9 9 
3 4 5 5 6 6 6 7 7 7 8 8 8 8 9 9 9 9 9 10 10 
3 4 5 5 6 6 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 
3 4 5 6 6 7 7 7 8 8 8 8 9 9 9 9 10 10 10 10 10 
4 5 5 6 6 7 7 8 8 8 9 9 9 9 10 10 10 10 10 11 11 
4 5 6 6 7 7 7 8 8 8 9 9 9 10 10 10 10 11 11 11 11 
4 5 6 6 7 7 8 8 8 9 9 9 10 10 10 10 11 11 11 11 11 
4 5 6 7 7 8 8 8 9 9 9 10 10 10 10 11 11 11 11 12 12 
4 5 6 7 7 8 8 9 9 9 10 10 10 10 11 11 11 11 12 12 12 
5 6 6 7 7 8 8 9 9 9 10 10 10 11 11 11 11 12 12 12 12 
5 6 7 7 8 8 9 9 9 10 10 10 11 11 11 11 12 12 12 12 13 
5 6 7 7 8 8 9 9 10 10 10 11 11 11 11 12 12 12 12 13 13 
5 6 7 8 8 9 9 9 10 10 10 11 11 11 12 12 12 12 13 13 13 
5 6 7 8 8 9 9 10 10 10 11 11 11 12 12 12 12 13 13 13 13 
5 6 7 8 8 9 9 10 10 10 11 11 11 12 12 12 13 13 13 13 14 
