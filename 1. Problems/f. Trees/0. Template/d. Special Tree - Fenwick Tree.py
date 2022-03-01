class FenwickTree():
    def __init__(self, N):
        self.N = N
        self.bit = [0 for i in range(N+1)]
        
    def add(self, index, value): # add `value` to self.data[index]
        index += 1
        while index <= self.N:
            self.bit[index] += value
            index += (index & -index)

    def prefixSum(self, index):
        index += 1
        ans = 0
        while index != 0:
            ans += self.bit[index]
            index -= (index & -index)
        return ansx
