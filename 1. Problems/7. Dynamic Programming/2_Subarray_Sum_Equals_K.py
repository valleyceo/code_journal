#LC 560. Subarray Sum Equals K
'''
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2
 

Constraints:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0] = 1
        psum = 0
        res = 0
        
        for n in nums:
            psum += n
            key = psum - k
            if key in d:
                res += d[key]
            
            d[psum] += 1
            
        return res