// Next Permutation

/*
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
*/

// my solution
class Solution {
public:
    void nextPermutation(vector<int>& nums) {
        int idx = -1;
        
        // find the first xi<xi+1 from end
        for (int i = nums.size() - 2; i >= 0; i--) {
            if (nums[i] < nums[i + 1]) {
                idx = i;
                break;
            }
        }
        
        // if none found, reverse whole sequence
        if (idx == -1) {
            reverse(nums.begin(), nums.end());
            return;
        }
        
        // find first x[idx] < xi, swap the two and reverse x[idx+1:end]
        int idx2 = -1;
        for (int i = nums.size()-1; i > idx; i--) {
            if (nums[i] > nums[idx]) {
                idx2 = i;
                break;
            }
        }
        
        swap(nums[idx], nums[idx2]);
        reverse(nums.begin() + idx + 1, nums.end());
        
        return;
    }
};