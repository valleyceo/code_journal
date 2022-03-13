# Also known as Binary Index Tree
class FenwickTree():
    def __init__(self, N):
        self.N = N
        self.bit = [0 for i in range(N+1)]

    # add val to self.data[index]
    def update(self, index, value):
        index += 1
        while index <= self.N:
            self.bit[index] += value
            index += (index & -index)

    def query(self, index):
        index += 1
        ans = 0
        while index != 0:
            ans += self.bit[index]
            index -= (index & -index)
        return ans

'''
Alternative
'''
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
