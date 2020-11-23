"""
LC 658 Find K Closest Elements

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b
 

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]
 

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 104
Absolute value of elements in the array and x will not exceed 10^4
"""
# Optimal log(n)+k
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        closestIdx = self.searchClosest(arr, x)
        left = closestIdx - 1
        right = closestIdx + 1
        res = [arr[closestIdx]]
        
        for _ in range(k-1):
            if left >= 0 and right < len(arr):
                if abs(arr[left]-x) <= abs(arr[right]-x):
                    res = [arr[left]] + res
                    left -= 1
                else:
                    res += [arr[right]]
                    right += 1
            elif left >= 0:
                res = [arr[left]] + res
                left -= 1
            else:
                res += [arr[right]]
                right += 1
                
        return res
    
    def searchClosest(self, arr: List[int], n) -> int:
        left = 0
        right = len(arr) - 1
        mid = 0
        
        while left < right:
            mid = left + (right-left)//2
            print(mid)
            if arr[mid] == n:
                return mid
            elif arr[mid] < n:
                left = mid + 1
            else:
                right = mid
        
        if mid > 0 and abs(n-arr[mid-1]) <= abs(n-arr[mid]):
            return mid-1
        elif mid < len(arr)-1 and abs(n-arr[mid+1]) < abs(n-arr[mid]):
            return mid+1
        else:
            return mid