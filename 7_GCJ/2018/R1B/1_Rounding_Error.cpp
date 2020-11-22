// Rounding Error

/*
Link:
https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard

- N people
- Percentage of each language
- Pick the highest percentage

INPUT:
 - # test
 - N (# Numper of people), L (# number of languages)
 - L integers Ci (i-th of people who uses the language)
*/

// my solution
#include <iostream>
#include <string>
#include <vector>
#include <queue>

using namespace std;

float round_up(float var)
{
    float value = (int)(var + .5);
    return (float)value / 100;
}


int main()
{
	int T, n;
	T = 1;
	
	std::cin >> n;

	while (T <= n)
	{
		int N, L;
		int n;
		double num, perc;

		int sum = 0;
		int remaining_ppl;

        std::cin >> N >> L;
        std::priority_queue<int> que;

        float d = 100.0 / (float)N;
        //float frac = d - (float)((int)d);
        remaining_ppl = N;

        // push in current survey
        for (int i = 0; i < L; i++) 
        {
        	std::cin >> n;
        	que.push(n);
        	remaining_ppl -= n;
        }

        // allocate the remaining
        while (remaining_ppl) 
        {
        	if (que.empty()) {
        		num = 1;
        		remaining_ppl -= 1;
        	} else {
        		num = que.front();
        	}

        	perc = (float)num * d;

        	while (remaining_ppl && (perc - (long)(perc)) < 0.5) {
        		num += 1;
        		perc = num * d;
        		remaining_ppl -= 1;
        	}

        	if (!que.empty()){
        		que.pop();
        	}
        	
        	sum += (int)(perc + 0.5);
        	//cout << sum << " " << perc << " next: " ;
        }
        
        //cout << endl << "remaining survey: ";
        // sum remaining
        while (!que.empty()) {
            //cout << que.front() << " ";
        	perc = d * que.front();
        	sum += (int)(perc + 0.5);
        	que.pop();
        }
        
        //cout << endl << "remaining ppl: ";
        while (remaining_ppl > 0) {
            num += 1;
            remaining_ppl -= 1;
    		perc = num * d;
    		
    		while (remaining_ppl && (perc - (long)(perc)) < 0.5) {
        		num += 1;
        		remaining_ppl -= 1;
        		
        		perc = num * d;
        	}
        	
        	sum += (int)(perc + 0.5);
        }
        
		std::cout << "Case #" << std::to_string(T) << ": " << sum << '\n';
		T++;
	}
	
	return 0;
}