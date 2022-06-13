# LC 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

'''
Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.

Example 1:

Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.
'''

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        return self.twoDequeSolution(nums, limit)

    # O(NlogN) time | O(N) space
    def heapSolution(self, nums: List[int], limit: int) -> int:
        max_heap = []
        min_heap = []
        res = 0
        min_idx = 0

        for i, n in enumerate(nums):
            heapq.heappush(max_heap, [-n, i])
            heapq.heappush(min_heap, [n, i])

            while -max_heap[0][0] - min_heap[0][0] > limit:
                min_idx = min(max_heap[0][1], min_heap[0][1]) + 1

                while max_heap[0][1] < min_idx:
                    heapq.heappop(max_heap)

                while min_heap[0][1] < min_idx:
                    heapq.heappop(min_heap)

            res = max(res, i - min_idx + 1)

        return res

    # O(n) time | O(n) space
    def twoDequeSolution(self, nums: List[int], limit: int) -> int:

        max_dq = deque()
        min_dq = deque()
        i = 0

        for n in nums:
            while len(max_dq) and n > max_dq[-1]:
                max_dq.pop()

            while len(min_dq) and n < min_dq[-1]:
                min_dq.pop()

            max_dq.append(n)
            min_dq.append(n)

            if max_dq[0] - min_dq[0] > limit:

                if max_dq[0] == nums[i]:
                    max_dq.popleft()

                if min_dq[0] == nums[i]:
                    min_dq.popleft()

                i += 1

        return len(nums) - i
