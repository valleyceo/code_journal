// K Empty Slots

/*
There is a garden with N slots. In each slot, there is a flower. The N flowers will bloom one by one in N days. In each day, there will be exactly one flower blooming and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N. Each number in the array represents the place where the flower will open in that day.

For example, flowers[i] = x means that the unique flower that blooms at day i will be at position x, where i and x will be in the range from 1 to N.

Also given an integer k, you need to output in which day there exists two flowers in the status of blooming, and also the number of flowers between them is k and these flowers are not blooming.

If there isn't such day, output -1.

Example 1:

Input: 
flowers: [1,3,2]
k: 1

Output: 2
Explanation: In the second day, the first and the third flower have become blooming.
Example 2:
Input: 

flowers: [1,2,3]
k: 1
Output: -1

Limit:
The given array will be in the range [1, 20000].

Note:
[1 5 3 2 4]

[1 4 3 5 2], k = 1
-> 3
* for each day, iterate through and find k empty slots between two blooms
* find the first (earliest) day it happens

*/

class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        if (k >= flowers.size()) 
            return -1;
        
        vector<int> bloom (flowers.size());
        
        for (int i = 0; i < flowers.size(); i++) {
            bloom[flowers[i]-1] = i;
        }
        
        int res = INT_MAX;
        
        for (int i = 0; i < flowers.size() - k - 1; i++) {
            int min = max(bloom[i], bloom[i + k + 1]); // since between value has to be k
            bool is_empty = true;
            
            // check if a plant has bloomed between the two slot
            for (int j = i + 1; j < i + k + 1; j++) {
                if (bloom[j] < min) {
                    is_empty = false;
                    break;
                }
            }
            
            if (is_empty && min < res) {
                res = min;
            }
                
        }
        
        return (res < flowers.size()) ? res + 1 : -1;
    }
};