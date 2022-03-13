# LC 1756. Design Most Recently Used Queue

'''
Design a queue-like data structure that moves the most recently used element to the end of the queue.

Implement the MRUQueue class:

MRUQueue(int n) constructs the MRUQueue with n elements: [1,2,3,...,n].
int fetch(int k) moves the kth element (1-indexed) to the end of the queue and returns it.

Example 1:

Input:
["MRUQueue", "fetch", "fetch", "fetch", "fetch"]
[[8], [3], [5], [2], [8]]
Output:
[null, 3, 6, 2, 2]

Explanation:
MRUQueue mRUQueue = new MRUQueue(8); // Initializes the queue to [1,2,3,4,5,6,7,8].
mRUQueue.fetch(3); // Moves the 3rd element (3) to the end of the queue to become [1,2,4,5,6,7,8,3] and returns it.
mRUQueue.fetch(5); // Moves the 5th element (6) to the end of the queue to become [1,2,4,5,7,8,3,6] and returns it.
mRUQueue.fetch(2); // Moves the 2nd element (2) to the end of the queue to become [1,4,5,7,8,3,6,2] and returns it.
mRUQueue.fetch(8); // The 8th element (2) is already at the end of the queue so just return it.
'''
class MRUQueue:

    def __init__(self, n: int):
        self.n = n
        self.tree = BIT(n + 2000)
        self.vals = [0] * (n + 2000)

        for i in range(n):
            self.tree.update(i, 1)
            self.vals[i] = i + 1

    def fetch(self, k: int) -> int:
        low = 0
        high = self.n

        while low < high:
            mid = (low + high) // 2

            if self.tree.query(mid) < k:
                low = mid + 1
            else:
                high = mid

        self.tree.update(low - 1, -1)
        self.tree.update(self.n, 1)
        self.vals[self.n] = self.vals[low - 1]
        self.n += 1

        return self.vals[low - 1]


# Your MRUQueue object will be instantiated and called as such:
# obj = MRUQueue(n)
# param_1 = obj.fetch(k)

class BIT():
    def __init__(self, N):
        self.N = N
        self.nums = [0 for i in range(N+1)]

    # add val to self.data[index]
    def query(self, k: int) -> int:
        ans = 0
        while k:
            ans += self.nums[k]
            k &= k-1
        return ans

    def update(self, k: int, x: int) -> int:
        k += 1
        while k < len(self.nums):
            self.nums[k] += x
            k += k & -k
