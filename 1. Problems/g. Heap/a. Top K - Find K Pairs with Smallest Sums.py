# LC 373. Find K Pairs with Smallest Sums

'''
You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
'''
# O(klogk) time | O(k) space
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:

        queue = [(nums1[0] + nums2[0], 0, 0)]
        res = []

        while queue and k > 0:
            val, i, j = heapq.heappop(queue)
            res.append([nums1[i], nums2[j]])

            if j < len(nums2) - 1:
                heapq.heappush(queue, (nums1[i] + nums2[j + 1], i, j + 1))

            if j == 0 and i < len(nums1) - 1:
                heapq.heappush(queue, (nums1[i + 1] + nums2[j], i + 1, j))

            k -= 1

        return res
