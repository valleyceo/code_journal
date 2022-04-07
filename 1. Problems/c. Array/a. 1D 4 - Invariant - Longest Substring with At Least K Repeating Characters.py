# LC 395. Longest Substring with At Least K Repeating Characters

'''
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each character in this substring is greater than or equal to k.

Example 1:

Input: s = "aaabb", k = 3
Output: 3
Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.

Example 2:

Input: s = "ababbc", k = 2
Output: 5
Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
'''

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        return self.slidingWindow(s, k)

    # O(N^2) time | O(N) space
    def divideConquer(self, s: str, k: int) -> int:

        def solve(start, end):
            if end < k:
                return 0

            counter = defaultdict(int)

            for i in range(start, end):
                counter[ord(s[i]) - ord('a')] += 1

            for i in range(start, end):
                if counter[ord(s[i]) - ord('a')] >= k:
                    continue

                mid = i
                mid_next = mid + 1

                while (mid_next < end and counter[ord(s[mid_next]) - ord('a')] < k):
                    mid_next += 1

                return max(solve(start, mid), solve(mid_next, end))

            return (end - start)

        return solve(0, len(s))

    # O(26 * N) time | O(26 * N) space
    def slidingWindow(self, s: str, k: int) -> int:
        max_unique = len(set(s))
        res = 0

        for curr_unique in range(1, max_unique + 1):
            count_map = [0] * 26
            head = 0
            tail = 0
            idx = 0
            unique = 0
            valid_count = 0

            while head < len(s):

                # Expand
                if unique <= curr_unique:
                    idx = ord(s[head]) - ord('a')

                    if count_map[idx] == 0:
                        unique += 1

                    count_map[idx] += 1

                    if count_map[idx] == k:
                        valid_count += 1

                    head += 1
                # Shrink
                else:
                    idx = ord(s[tail]) - ord('a')

                    if count_map[idx] == k:
                        valid_count -= 1

                    count_map[idx] -= 1

                    if count_map[idx] == 0:
                        unique -= 1

                    tail += 1

                if unique == curr_unique and unique == valid_count:
                    res = max(res, head - tail)

        return res
