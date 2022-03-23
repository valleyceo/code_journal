# LC 698. Partition to K Equal Sum Subsets

'''
Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4,3,2,3,5,2,1], k = 4
Output: true
Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

Example 2:

Input: nums = [1,2,3,4], k = 3
Output: false
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        return self.V3memoBitmasking(nums, k)

    def V3memoBitmasking(self, arr: List[int], k: int) -> bool:
        total_array_sum = sum(arr)
        n = len(arr)

        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k
        arr.sort(reverse = True)
        mask = 0
        memo = {}

        def backtrack(idx, count: int, curr_sum: int) -> bool:
            nonlocal mask
            n = len(arr)

            if count == k - 1:
                return True

            if curr_sum > target_sum:
                return False

            if mask in memo:
                return memo[mask]

            if curr_sum == target_sum:
                memo[mask] = backtrack(0, count + 1, 0)
                return memo[mask]

            for j in range(idx, n):
                if ((mask >> j) & 1) == 0:
                    mask |= (1 << j)

                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True

                    mask ^= (1 << j)

            memo[mask] = False
            return memo[mask]

        return backtrack(0, 0, 0)

    def V2memoization(self, arr: List[int], k: int) -> bool:
        total_array_sum = sum(arr)
        n = len(arr)

        if total_array_sum % k != 0:
            return False

        target_sum = total_array_sum // k
        arr.sort(reverse = True)
        taken = ['0'] * n
        memo = {}

        def backtrack(idx, count: int, curr_sum: int) -> bool:
            n = len(arr)
            taken_str = "".join(taken)

            if count == k - 1:
                return True

            if curr_sum > target_sum:
                return False

            if taken_str in memo:
                return memo[taken_str]

            if curr_sum == target_sum:
                memo[taken_str] = backtrack(0, count + 1, 0)
                return memo[taken_str]

            for j in range(idx, n):
                if taken[j] == '0':
                    taken[j] = '1'

                    if backtrack(j + 1, count, curr_sum + arr[j]):
                        return True

                    taken[j] = '0'

            memo[taken_str] = False
            return memo[taken_str]

        return backtrack(0, 0, 0)

    def V1TLEbacktracking(self, nums: List[int], k: int) -> bool:
        def dfs(idx):
            if idx == len(nums):
                return True

            for i in range(k):
                if nums[idx] <= target[i]:
                    target[i] -= nums[idx]

                    if dfs(idx + 1):
                        return True

                    target[i] += nums[idx]

            return False

        if len(nums) < k:
            return False

        total = sum(nums)
        nums.sort(reverse = True)

        if total % k != 0:
            return False

        target = [total / k] * k

        return dfs(0)
