# 567. Permutation in String

'''
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.slidingWindowOptimized(s1, s2)

    # O(n1 + 26*(n2-n1)) time | O(1) space
    def slidingWindow(self, s1: str, s2: str) -> bool:
        def isMatch(arr1, arr2) -> bool:
            for a1, a2 in zip(arr1, arr2):
                if a1 != a2:
                    return False

            return True

        if len(s1) > len(s2):
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26
        ord_a = ord('a')

        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord_a] += 1
            s2_map[ord(s2[i]) - ord_a] += 1

        for i in range(len(s1), len(s2)):
            if isMatch(s1_map, s2_map):
                return True

            s2_map[ord(s2[i]) - ord_a] += 1
            s2_map[ord(s2[i - len(s1)]) - ord_a] -= 1

        return isMatch(s1_map, s2_map)

    # O(n1 + (n2-n1)) = O(n2) time | O(1) space
    def slidingWindowOptimized(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_map = [0] * 26
        s2_map = [0] * 26
        ord_a = ord('a')

        for i in range(len(s1)):
            s1_map[ord(s1[i]) - ord_a] += 1
            s2_map[ord(s2[i]) - ord_a] += 1

        match_count = 0

        for i in range(26):
            if s1_map[i] == s2_map[i]:
                match_count += 1

        for i in range(len(s1), len(s2)):
            left = ord(s2[i - len(s1)]) - ord_a
            right = ord(s2[i]) - ord_a

            if match_count == 26:
                return True

            s2_map[right] += 1

            if s2_map[right] == s1_map[right]:
                match_count += 1
            elif s2_map[right] == s1_map[right] + 1:
                match_count -= 1

            s2_map[left] -= 1

            if s2_map[left] == s1_map[left]:
                match_count += 1
            elif s2_map[left] == s1_map[left] - 1:
                match_count -= 1

        return match_count == 26
