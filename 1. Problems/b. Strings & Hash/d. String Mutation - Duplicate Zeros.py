# 1089. Duplicate Zeros

'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:
1 <= arr.length <= 10^4
0 <= arr[i] <= 9
'''
# O(n) time | O(1) space
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        n = len(arr)
        zeros = arr.count(0)
        widx = n - 1 + zeros

        for i in range(n - 1, -1, -1):
            if arr[i] != 0:
                if widx < n:
                    arr[widx] = arr[i]
            else:
                if widx < n:
                    arr[widx] = arr[i]

                widx -= 1

                if widx < n:
                    arr[widx] = arr[i]

            widx -= 1
