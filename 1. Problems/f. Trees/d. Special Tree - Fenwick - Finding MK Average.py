# LC 1825. Finding MK Average

'''
You are given two integers, m and k, and a stream of integers. You are tasked to implement a data structure that calculates the MKAverage for the stream.

The MKAverage can be calculated using these steps:

If the number of the elements in the stream is less than m you should consider the MKAverage to be -1. Otherwise, copy the last m elements of the stream to a separate container.
Remove the smallest k elements and the largest k elements from the container.
Calculate the average value for the rest of the elements rounded down to the nearest integer.
Implement the MKAverage class:

MKAverage(int m, int k) Initializes the MKAverage object with an empty stream and the two integers m and k.
void addElement(int num) Inserts a new element num into the stream.
int calculateMKAverage() Calculates and returns the MKAverage for the current stream rounded down to the nearest integer.
'''

class Fenwick:
    def __init__(self, n: int):
        self.nums = [0] * (n + 1)

    def sum(self, k: int) -> int:
        k += 1
        res = 0

        while k:
            res += self.nums[k]
            k &= k - 1          # unset last bit

        return res

    def add(self, k: int, x: int) -> None:
        k += 1

        while k < len(self.nums):
            self.nums[k] += x
            k += k & -k

class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.data = deque()
        self.value = Fenwick(10**5 + 1)
        self.index = Fenwick(10**5 + 1)

    def addElement(self, num: int) -> None:
        self.data.append(num)
        self.value.add(num, num)
        self.index.add(num, 1)

        if len(self.data) > self.m:
            num = self.data.popleft()
            self.value.add(num, -num)
            self.index.add(num, -1)

    def calculateMKAverage(self) -> int:
        if len(self.data) < self.m:
            return -1

        left = self.getIndex(self.k)
        right = self.getIndex(self.m - self.k)
        res = self.value.sum(right) - self.value.sum(left)
        res += (self.index.sum(left) - self.k) * left
        res -= (self.index.sum(right) - (self.m - self.k)) * right

        return res // (self.m - 2 * self.k)

    def getIndex(self, k):
        left = 0
        right = 10**5 + 1

        while left < right:
            mid = left + right >> 1

            if self.index.sum(mid) < k:
                left = mid + 1
            else:
                right = mid

        return left


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
