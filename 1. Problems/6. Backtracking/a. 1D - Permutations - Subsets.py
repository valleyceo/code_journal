# LC 78. Subsets

'''
Given array of unique elements, return all possible subsets

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.bitmasking(nums)
    
    # Solution 1 Cascade - O(N * 2^N) Time | O(N * 2^N) space
    def cascade(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        output = [[]]
        
        for num in nums:
            output += [subset + [num] for subset in output]
            
        return output
    
    # Solution 2 Backtracking - O(N * 2^N) Time | O(N) space
    def backtrack(self, nums: List[int]) -> List[List[int]]:
        
        def backtrack(idx = 0, path = []):
            if len(path) == k:
                res.append(path[:])
                return
            
            for i in range(idx, n):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
                
            return
        
        res = []
        n = len(nums)
        
        for k in range(n+1):
            backtrack()
            
        return res
    
    # Solution 1 bitmasking - O(N * 2^N) Time | O(N * 2^N) space
    def bitmasking(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        
        for i in range(2**n, 2**(n+1)):
            bitmask = bin(i)[3:]
            res.append([nums[j] for j in range(n) if bitmask[j] == "1"])
        
        return res