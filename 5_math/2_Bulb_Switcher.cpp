// Bulb Switcher

/*
There are n bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb. Find how many bulbs are on after n rounds.

Example:

Input: 3
Output: 1 
Explanation: 
At first, the three bulbs are [off, off, off].
After first round, the three bulbs are [on, on, on].
After second round, the three bulbs are [on, off, on].
After third round, the three bulbs are [on, off, off]. 

So you should return 1, because there is only one bulb is on.

My note:
- n bulbs (all off)
- turn all on first run
- for ith round toggle every i bulb
- find how many bulbs are on after n rounds

ex. n = 1, 2
-> 1
ex. n = 3
-> 1

ex. n = 4
1: [1 1 1 1]
2: [1 0 1 0]
3: [1 0 0 0]
4: [1 0 0 1]
-> 2
ex. n = 5
1: [1 1 1 1 1]
2: [1 0 1 0 1]
3: [1 0 0 0 1]
4: [1 0 0 1 1]
5: [1 0 0 1 0]
-> 2

ex. n = 6~8 -> 2
ex. n = 9 -> 3

solution:
create n size dp array
for every inc num, add all multiples to dp array (or toggle)
return all 1s
-> does not work on 9999999 (TLE)

pattern: solution increases every x^2
mathematical solution -> find largest x such that x*x <= n
-> use binary search
*/

// my  - Time: O(n), Space: O(n)
class Solution {
public:
    int bulbSwitch(int n) {
        vector<long> dp(n, true);
        int res = 0;
        
        for (int i = 2; i <= n; i++) {
            for (int j = i; j <= n; j += i) {
                dp[j-1] ^= true;
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (dp[i]) res++;
        }
        
        return res;
    }
};

// optimal solution - Time: O(log(sqrt(n))), Space: O(1)
class Solution {
public:
    int bulbSwitch(int n) {
        if (n < 1) return 0;
        
        int start = 2, end = n, mid; // n = 1, 2 -> 1
        
        while (start < end) {
            mid = start + (end - start) / 2;
            
            if (mid <= n / mid) { // prevent overloading
                start = mid + 1;
            } else {
                end = mid;
            }
        }
        
        return start - 1;
    }
};