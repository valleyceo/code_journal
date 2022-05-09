# LC 895. Maximum Frequency Stack

'''
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]
'''

# O(1) time push/pop | O(N) space, stackmap
class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.stackmap = defaultdict(list)
        self.max_freq = 0

    def push(self, val: int) -> None:
        freq = self.freq[val] + 1
        self.freq[val] = freq

        if freq > self.max_freq:
            self.max_freq = freq

        self.stackmap[freq].append(val)

    def pop(self) -> int:
        val = self.stackmap[self.max_freq].pop()
        self.freq[val] -= 1

        if not self.stackmap[self.max_freq]:
            self.max_freq -= 1

        return val

"""
Note:
- for every push on same element, create a new list on stackmap on the next freq.
Stack map -> {1: [5, 7, 4], 2: [5, 7], 3: [5]})
Freq map -> {5: 3, 7: 2, 4: 1})
- Keep track of max freq
"""
