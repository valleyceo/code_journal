class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        return self.merge(left, right)
        
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        ll = len(left)
        lr = len(right)
        i1 = 0
        i2 = 0
        arr = []
        
        while i1 < ll and i2 < lr:
            if left[i1] <= right[i2]:
                arr.append(left[i1])
                i1 += 1
            else:
                arr.append(right[i2])
                i2 += 1
        
        arr += left[i1:] + right[i2:]
        
        return arr