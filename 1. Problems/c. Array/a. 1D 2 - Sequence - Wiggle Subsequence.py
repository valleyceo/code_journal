# 376. Wiggle Subsequence

'''
A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with one element and a sequence with two non-equal elements are trivially wiggle sequences.

For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) alternate between positive and negative.
In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences. The first is not because its first two differences are positive, and the second is not because its last difference is zero.
A subsequence is obtained by deleting some elements (possibly zero) from the original sequence, leaving the remaining elements in their original order.

Given an integer array nums, return the length of the longest wiggle subsequence of nums.

Example 1:

Input: nums = [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence with differences (6, -3, 5, -7, 3).

Example 2:

Input: nums = [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length.
One is [1, 17, 10, 13, 10, 16, 8] with differences (16, -7, 3, -3, 6, -8).

Example 3:

Input: nums = [1,2,3,4,5,6,7,8,9]
Output: 2
'''
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        return self.optimized(nums)

    def naive(self, nums: List[int]) -> int:
        idx = 0

        while idx < len(nums) - 1:
            if nums[idx] != nums[idx + 1]:
                if nums[idx] < nums[idx + 1]:
                    findLarge = True
                else:
                    findLarge = False

                break

            idx += 1

        if idx == len(nums) - 1:
            return 1

        prev_val = nums[idx]
        res = 0

        for n in nums[idx:]:
            if findLarge:
                if n > prev_val:
                    res += 1
                    prev_val = n
                    findLarge ^= True
                else:
                    prev_val = min(prev_val, n)
            else:
                if n < prev_val:
                    res += 1
                    prev_val = n
                    findLarge ^= True
                else:
                    prev_val = max(prev_val, n)

        return res + 1

    def optimized(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        diff = nums[1] - nums[0]
        count = 2 if diff != 0 else 1

        for i in range(2, len(nums)):
            next_diff = nums[i] - nums[i-1]

            if (diff <= 0 and next_diff > 0) or (diff >= 0 and next_diff < 0):
                count += 1
                diff = next_diff

        return count
