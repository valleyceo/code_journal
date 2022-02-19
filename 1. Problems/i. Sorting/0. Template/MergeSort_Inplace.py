# Mergesort in-place
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(0, len(nums)-1, nums)
        return nums
    
    def mergeSort(self, l: int, r: int, nums: List[int]):
        
        if l < r:
            m = l + (r-l)//2
            
            self.mergeSort(l, m, nums)
            self.mergeSort(m+1, r, nums)
            
            self.merge(l, m, r, nums)
            
        return
        
        
    def merge(self, l: int, m: int, r: int, nums: List[int]):
        
        start1 = l
        start2 = m+1
        
        if nums[m] <= nums[start2]:
            return
        
        while start1 <= m and start2 <= r:
            if nums[start1] <= nums[start2]:
                start1 += 1
            else:
                val = nums[start2]
                idx = start2
                
                while (idx != start1):
                    nums[idx] = nums[idx-1]
                    idx -= 1
                
                nums[start1] = val
                
                start1 += 1
                start2 += 1
                m += 1