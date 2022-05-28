# LC 1055. Shortest Way to Form String

'''
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
'''

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        return self.onePassSolution(source, target)

    # Two pointer
    # O(MN) time | O(1) space
    def twoPointer(self, source: str, target: str) -> int:
        res = 0
        t_idx = 0

        while t_idx < len(target):
            s_idx = 0
            flag = False

            while s_idx < len(source) and t_idx < len(target):
                if source[s_idx] == target[t_idx]:
                    s_idx += 1
                    t_idx += 1
                    flag = True
                else:
                    s_idx += 1

            if flag:
                res += 1
            else:
                return -1

        return res

    # Binary Search
    # O(N*log(M)) time | O(N) space
    def binarySearch(self, source: str, target: str) -> int:
        s_map = defaultdict(list)
        idx = 0
        res = 1

        def binarySearch(c, cidx):
            nonlocal res
            curr_list = s_map[c]

            if curr_list[-1] < cidx:
                res += 1
                cidx = 0

            left = 0
            right = len(curr_list) - 1

            while left < right:
                mid = (left + right) // 2

                if curr_list[mid] < cidx:
                    left = mid + 1
                else:
                    right = mid

            return curr_list[left] + 1

        for i, c in enumerate(source):
            s_map[c].append(i)

        for c in target:
            if c not in s_map:
                return -1
            else:
                idx = binarySearch(c, idx)

        return res

    # O(N + M) time | O(26*N)
    def onePassSolution(self, source: str, target: str) -> int:
        s_set = set(source)
        dp = [[-1] * len(source) for _ in range(26)]

        for i, c in enumerate(source):
            dp[ord(c) - ord('a')][i] = i

        for l in dp:

            pre = -1

            for i in range(len(l)-1, -1, -1):
                if l[i] != -1:
                    pre = l[i]
                else:
                    l[i] = pre

        res = 1
        idx = 0

        for c in target:
            if c not in s_set:
                return -1

            if idx >= len(source):
                idx = 0
                res += 1

            idx = dp[ord(c) - ord('a')][idx]

            if idx == -1:
                idx = dp[ord(c) - ord('a')][0]
                res += 1

            idx += 1

        return res
