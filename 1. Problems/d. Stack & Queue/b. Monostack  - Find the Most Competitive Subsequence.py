# LC 1673. Find the Most Competitive Subsequence

'''
Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.
'''
# O(n) time | O(n) space
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        queue = []
        surplus = len(nums) - k

        for n in nums:
            while queue and queue[-1] > n and surplus > 0:
                queue.pop()
                surplus -= 1

            queue.append(n)

        return queue[:k]
