# LC 281. Zigzag Iterator

'''
Given two vectors of integers v1 and v2, implement an iterator to return their elements alternately.

Implement the ZigzagIterator class:

ZigzagIterator(List<int> v1, List<int> v2) initializes the object with the two vectors v1 and v2.
boolean hasNext() returns true if the iterator still has elements, and false otherwise.
int next() returns the current element of the iterator and moves the iterator to the next element.

Example 1:

Input: v1 = [1,2], v2 = [3,4,5,6]
Output: [1,3,2,4,5,6]
Explanation: By calling next repeatedly until hasNext returns false, the order of elements returned by next should be: [1,3,2,4,5,6].

Example 2:

Input: v1 = [1], v2 = []
Output: [1]

Example 3:

Input: v1 = [], v2 = [1]
Output: [1]
'''
class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.e_idx = [0, 0]

        self.vcount = len(self.vectors)
        self.v_idx = 0

        self.count = len(v1) + len(v2)
        self.out_count = 0

    def next(self) -> int:
        if not self.hasNext():
            raise Exception

        while self.e_idx[self.v_idx] == len(self.vectors[self.v_idx]):
            self.v_idx = (self.v_idx + 1) % self.vcount

        idx = self.e_idx[self.v_idx]
        val = self.vectors[self.v_idx][idx]
        self.e_idx[self.v_idx] += 1
        self.v_idx = (self.v_idx + 1) % self.vcount
        self.out_count += 1

        return val

    def hasNext(self) -> bool:
        return self.out_count < self.count

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
