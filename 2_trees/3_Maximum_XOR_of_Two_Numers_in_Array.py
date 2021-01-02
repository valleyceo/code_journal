"""
Maximum XOR of Two Numbers in an Array

Given an integer array nums, return the maximum result of nums[i] XOR nums[j], where 0 ≤ i ≤ j < n.

Follow up: Could you do this in O(n) runtime?

Example 1:

Input: nums = [3,10,5,25,2,8]
Output: 28
Explanation: The maximum result is 5 XOR 25 = 28.
Example 2:

Input: nums = [0]
Output: 0
Example 3:

Input: nums = [2,4]
Output: 6
Example 4:

Input: nums = [8,10,2]
Output: 10
Example 5:

Input: nums = [14,70,53,83,49,91,36,80,92,51,66,70]
Output: 127
 
Constraints:

1 <= nums.length <= 2 * 10^4
0 <= nums[i] <= 2^31 - 1
"""
# Time complexity: O(N), Space complexity: O(N)
class Solution:
    class TrieNode:
        def __init__(self):
            self.next = {}
        
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = self.TrieNode()
        
        for n in nums:
            node = root
            for i in range(32, -1, -1):
                bit = (n >> i) & 1
                
                if bit not in node.next:
                    node.next[bit] = self.TrieNode()
                
                node = node.next[bit]
            
        maxXOR = 0
        
        for n in nums:
            node = root
            total = 0
            
            for i in range(32, -1, -1):
                bit = (n >> i) & 1
                
                if (bit^1) in node.next:
                    node = node.next[bit^1]
                    total += (1 << i)
                else:
                    node = node.next[bit]
            
            maxXOR = max(maxXOR, total)
            
        return maxXOR