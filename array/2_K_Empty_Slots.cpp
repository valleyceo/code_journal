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

Note:
The given array will be in the range [1, 20000].
*/

class Solution {
public:
    int kEmptySlots(vector<int>& flowers, int k) {
        if (k >= flowers.size())
            return -1;
        
        vector<int> bloom_order(flowers.size());
        
        for (int i = 0; i < flowers.size(); i++) {
            bloom_order[flowers[i] - 1] = i;
        }
        
        int best_ans = INT_MAX;
        
        for (int i = 0; i < flowers.size() - k - 1; i++) {
            
            int min = max(bloom_order[i], bloom_order[i+k+1]);
            bool is_empty = true;
            
            for (int j = i+1; j < i+k+1; j++) {
                if (bloom_order[j] < min) {
                    is_empty = false;
                    break;
                }
            }
            
            if (is_empty == true && min < best_ans) {
                best_ans = min;
            }
        }
        
        if (best_ans < flowers.size())
            return best_ans+1;
        else 
            return -1;
    }
};