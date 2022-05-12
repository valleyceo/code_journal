# LC 358. Rearrange String k Distance Apart

'''
Given a string s and an integer k, rearrange s such that the same characters are at least distance k from each other. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least a distance of 3 from each other.

Example 2:

Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.

Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least a distance of 2 from each other.
'''
# O(N) time | O(N) space
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        n = len(s)

        if not k:
            return s

        counter = Counter(s)
        queue = [[-val, char] for char, val in counter.items()]
        heapq.heapify(queue)

        prev = deque()
        res = []

        while queue:

            count, char = heapq.heappop(queue)
            res.append(char)

            count += 1
            prev.append([count, char])

            if len(prev) == k:
                prev_max = prev.popleft()

                if prev_max[0] < 0:
                    heapq.heappush(queue, prev_max)

        if len(res) < len(s):
            return ""

        return "".join(res)

"""
Insight:
- Need two data structures:
    - Heap -> Use the most frequent first to sparse each chars as far as possible
    - Deque -> Send chars to deque after using, such that it can only be reused after k (or when deque length is k)
"""
