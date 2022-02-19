"""
Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Returns the element representing the kth largest element in the stream.
"""
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = []
        self.k = k

        for n in nums:
            heapq.heappush(self.q, n)

        while len(self.q) > self.k:
            heapq.heappop(self.q)

    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)

        while len(self.q) > self.k:
            heapq.heappop(self.q)

        return self.q[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
