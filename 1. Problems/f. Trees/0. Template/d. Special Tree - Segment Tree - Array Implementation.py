# limit for array size
N_MAX = 20 # 10000

class SegmentTree:
    def __init__(self, arr):

        self.n = len(arr)
        self.tree = [0] * (2 * N_MAX) # Max size of tree

        # insert leaf nodes in tree
        for i in range(self.n) :
            self.tree[self.n + i] = arr[i]

        # build the tree by calculating parents
        for i in range(self.n - 1, 0, -1) :
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    # function to update a tree node
    def updateTreeNode(self, p, value) :

        # set value at position p
        self.tree[p + self.n] = value
        p = p + self.n

        # move upward and update parents
        i = p

        while i > 1:
            self.tree[i >> 1] = self.tree[i] + self.tree[i ^ 1]
            i >>= 1

    # function to get sum on interval [l, r)
    def query(self, l, r) :

        res = 0
        l += self.n # loop to find the sum in the range
        r += self.n

        while l < r :

            if (l & 1):
                res += self.tree[l]
                l += 1

            if (r & 1):
                r -= 1
                res += self.tree[r]

            l >>= 1
            r >>= 1

        return res

# Test code
if __name__ == "__main__" :

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    st = SegmentTree(a)

    # print the sum in range(1,2) index-based
    print(st.query(1, 3)) # -> 5

    # modify element at 2nd index
    st.updateTreeNode(2, 1)

    # print the sum in range(1,2) index-based
    print(st.query(1, 3)) # -> 3
