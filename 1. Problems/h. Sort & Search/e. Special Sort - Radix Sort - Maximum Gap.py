# 164. Maximum Gap

'''
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Example 1:

Input: nums = [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either (3,6) or (6,9) has the maximum difference 3.

Example 2:

Input: nums = [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
'''
class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        return self.bucketSortSolution(nums)

    def naiveSolution(self, nums: List[int]) -> int:
        maxDiff = 0
        nums.sort()

        for i in range(1, len(nums)):
            diff = nums[i] - nums[i-1]
            maxDiff = max(maxDiff, diff)

        return maxDiff

    def radixSortSolution(self, nums: List[int]) -> int:

        def radixSort(arr):
            maxVal = max(arr)
            exp = 1
            radix = 10

            aux = [0] * len(arr)

            while maxVal // exp > 0:
                count = [0] * radix

                for i in range(len(arr)):
                    count[arr[i]//exp % 10] += 1

                for i in range(1, len(count)):
                    count[i] += count[i-1]

                for i in range(len(arr) - 1, -1, -1):
                    count[(arr[i]//exp) % 10] -= 1
                    aux[count[(arr[i]//exp) % 10]] = arr[i]

                for i in range(len(arr)):
                    arr[i] = aux[i]

                exp *= 10

        if len(nums) < 2:
            return 0

        radixSort(nums)
        res = 0

        for i in range(1, len(nums)):
            res = max(res, nums[i] - nums[i-1])

        return res

    def bucketSortSolution(self, nums: List[int]) -> int:
        class Bucket:
            def __init__(self):
                self.used = False
                self.minval = float('inf')
                self.maxval = float('-inf')

        if len(nums) < 2:
            return 0

        min_val = min(nums)
        max_val = max(nums)

        bucket_size = max(1, (max_val - min_val) // (len(nums) - 1))
        bucket_num = (max_val - min_val) // bucket_size + 1
        buckets = [Bucket() for _ in range(bucket_num)]

        for n in nums:
            idx = (n - min_val) // bucket_size

            buckets[idx].used = True
            buckets[idx].minval = min(buckets[idx].minval, n)
            buckets[idx].maxval = max(buckets[idx].maxval, n)

        prev_max = min_val
        res = 0

        for bucket in buckets:
            if not bucket.used:
                continue

            res = max(res, bucket.minval - prev_max)
            prev_max = bucket.maxval

        return res
