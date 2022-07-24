# LC 2035. Partition Array Into Two Arrays to Minimize Sum Difference

'''
You are given an integer array nums of 2 * n integers. You need to partition nums into two arrays of length n to minimize the absolute difference of the sums of the arrays. To partition nums, put each element of nums into one of the two arrays.

Return the minimum possible absolute difference.

Example:
Input: nums = [3,9,7,3]
Output: 2
Explanation: One optimal partition is: [3,9] and [7,3].
The absolute difference between the sums of the arrays is abs((3 + 9) - (7 + 3)) = 2.
'''
class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        return self.divideSolution(nums)

    def tleSolution(self, nums: List[int]) -> int:
        n = len(nums)
        res = float('inf')

        def backtrack(idx, left, path_sum, rem_sum):
            nonlocal res

            if n - idx == left:
                path_sum += sum(nums[idx:])
                rem_sum -= sum(nums[idx:])
                res = min(res, abs(path_sum - rem_sum))
                return
            
            if idx >= n:
                return

            backtrack(idx + 1, left - 1, path_sum + nums[idx], rem_sum - nums[idx])
            backtrack(idx + 1, left, path_sum, rem_sum)

        backtrack(0, n // 2, 0, sum(nums))
        return res

    def divideSolution(self, nums: List[int]) -> int:
        n = len(nums)
        nh = len(nums) // 2

        def combination_sums(arr):
            dp = {}

            for ct in range(1, len(arr)):
                combination_sums = []

                for comb in combinations(arr, ct):
                    combination_sums.append(sum(comb))

                dp[ct] = combination_sums

            return dp

        left_arr = nums[:nh]
        right_arr = nums[nh:]
        left_dp = combination_sums(left_arr)
        right_dp = combination_sums(right_arr)
        res = abs(sum(left_arr) - sum(right_arr))
        total = sum(nums)
        half = total // 2

        for left_count in range(1, nh):
            right_count = nh - left_count
            left_cs = left_dp[left_count]
            right_cs = right_dp[right_count]
            right_cs.sort()

            for ls in left_cs:
                need = half - ls
                idx = bisect.bisect_left(right_cs, need)

                if idx < len(right_cs):
                    left_sum = ls + right_cs[idx]
                    right_sum = total - left_sum
                    res = min(res, abs(left_sum - right_sum))

                if idx > 0:
                    left_sum = ls + right_cs[idx - 1]
                    right_sum = total - left_sum
                    res = min(res, abs(left_sum - right_sum))

        return res
