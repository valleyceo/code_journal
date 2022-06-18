# LC 632. Smallest Range Covering Elements from K Lists

'''
You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
'''
# O(nlogn) time | O(n) space
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        heap = []
        right = float('-inf')

        for i in range(n):
            heapq.heappush(heap, (nums[i][0], i, 0))
            right = max(right, nums[i][0])

        res = [float('-inf'), right]
        min_dist = float('inf')

        while heap:
            val, row, col = heapq.heappop(heap)

            if right - val < min_dist:
                min_dist = right - val
                res = [val, right]

            if col + 1 == len(nums[row]):
                break

            right = max(right, nums[row][col + 1])
            heapq.heappush(heap, (nums[row][col + 1], row, col + 1))

        return res
