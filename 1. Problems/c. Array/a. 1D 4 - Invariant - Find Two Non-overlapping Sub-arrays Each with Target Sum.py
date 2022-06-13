# LC 1477. Find Two Non-overlapping Sub-arrays Each With Target Sum

'''
You are given an array of integers arr and an integer target.

You have to find two non-overlapping sub-arrays of arr each with a sum equal target. There can be multiple answers so you have to find an answer where the sum of the lengths of the two sub-arrays is minimum.

Return the minimum sum of the lengths of the two required sub-arrays, or return -1 if you cannot find such two sub-arrays.

Example 1:

Input: arr = [3,2,2,4,3], target = 3
Output: 2
Explanation: Only two sub-arrays have sum = 3 ([3] and [3]). The sum of their lengths is 2.
'''
class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        return self.prefixSum(arr, target)

    def prefixSum(self, arr: List[int], target: int) -> int:
        prefix = {0: -1}
        prefsum_arr = arr.copy()
        dp = [float('inf')] * len(arr)
        res = float('inf')
        best = float('inf')

        for i in range(1, len(arr)):
            prefsum_arr[i] += prefsum_arr[i-1]

        for i, n in enumerate(prefsum_arr):
            if n - target in prefix:
                prev = prefix[n - target]

                if prev > -1:
                    res = min(res, i - prev + dp[prev])

                best = min(best, i - prev)

            dp[i] = best
            prefix[n] = i

        return -1 if res == float('inf') else res

    def mySolution(self, arr: List[int], target: int) -> int:
        dp_left = [float('inf')] * (len(arr) + 1)
        dp_right = [float('inf')] * (len(arr) + 1)
        moving_sum = 0
        moving_queue = deque()

        for i, n in enumerate(arr):
            dp_left[i + 1] = dp_left[i]

            while moving_queue and moving_sum + n > target:
                val = moving_queue.popleft()
                moving_sum -= val

            if n > target:
                continue

            moving_sum += n
            moving_queue.append(n)

            if moving_sum == target:
                dp_left[i + 1] = min(dp_left[i + 1], len(moving_queue))

        moving_sum = 0
        moving_queue = deque()

        for i in range(len(arr) - 1, -1, -1):
            n = arr[i]
            dp_right[i] = dp_right[i + 1]

            while moving_queue and moving_sum + n > target:
                val = moving_queue.popleft()
                moving_sum -= val

            if n > target:
                continue

            moving_sum += n
            moving_queue.append(n)

            if moving_sum == target:
                dp_right[i] = min(dp_right[i], len(moving_queue))

        res = float('inf')

        for i in range(1, len(arr)):
            if dp_left[i] < float('inf') and dp_right[i] < float('inf'):
                res = min(res, dp_left[i] + dp_right[i])

        return res if res < float('inf') else -1
