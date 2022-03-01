# LC 907. Sum of Subarray Minimums

'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation:
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
'''

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        return self.onePass(arr)

    def readable(self, arr: List[int]) -> int:
        n = len(arr)
        mod = 10 ** 9 + 7
        left = [0] * n
        right = [0] * n

        stack = []
        for i in range(n):
            count = 1

            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]

            left[i] = count
            stack.append([arr[i], count])

        stack = []
        for i in range(n - 1, -1, -1):
            count = 1

            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]

            right[i] = count
            stack.append([arr[i], count])

        return sum([a*l*r for a, l, r in zip(arr, left, right)]) % mod

    # O(n) Monotone
    def onePass(self, arr: List[int]) -> int:
        mod = 10 ** 9 + 7
        A = [0] + arr + [0]
        stack = []
        res = 0

        for i, val in enumerate(A):

            while stack and A[stack[-1]] > val:
                midIdx = stack.pop()
                prevIdx = stack[-1]
                res += A[midIdx] * (i - midIdx) * (midIdx - prevIdx)

            stack.append(i)

        return res % mod
