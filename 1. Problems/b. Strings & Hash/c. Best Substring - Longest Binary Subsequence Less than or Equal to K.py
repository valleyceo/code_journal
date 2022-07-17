# 2311. Longest Binary Subsequence Less Than or Equal to K

'''
You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
'''

# Greedy solution, O(N) time | O(1) space
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        num = 0
        num_ct = 0
        power = 1

        for i, c in reversed(list(enumerate(s))):

            if c == "1":
                num += power

            if num > k:
                count = 0

                for j in range(i):
                    if s[j] == "0":
                        count += 1

                return num_ct + count

            num_ct += 1
            power *= 2

        return len(s)

"""
Algorithm:
- Find the substring from right until it is bigger than k
- Count the number plus all '0' afterwards

Analysis:
- Why does this work? Greedy solution works because for the right number, whenever you try to add another "1" to maximise length, you will have to remove a "0", which as a result does not maximise length. Thus, greedily finding the first k below number works.
"""
