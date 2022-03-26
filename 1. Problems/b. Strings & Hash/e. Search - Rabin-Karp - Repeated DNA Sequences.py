# LC 187. Repeated DNA Sequences

'''
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        return self.rollingHash(s)

    # Rabin-Karp rolling hash solution
    def rollingHash(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        ch_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        hash_base = 4
        seen = set()
        res = set()
        moving_hash = 0

        for i in range(10):
            moving_hash = moving_hash * hash_base + ch_map[s[i]]

        seen.add(moving_hash)
        last_hash_power = hash_base ** 9

        for i in range(10, len(s)):
            moving_hash = (moving_hash - (ch_map[s[i-10]] * last_hash_power)) * hash_base + ch_map[s[i]]

            if moving_hash in seen:
                res.add(s[i - 9:i + 1])

            seen.add(moving_hash)

        return res

    def bitmaskSolution(self, s: str) -> List[str]:
        if len(s) <= 10:
            return []

        L = 10
        ch_map = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [ch_map[c] for c in s]
        seen = set()

        bitmask = 0

        for i in range(L):
            bitmask <<= 2
            bitmask |= nums[i]

        seen.add(bitmask)
        res = set()

        for i in range(L, len(s)):
            bitmask <<= 2
            bitmask |= nums[i]
            bitmask &= ~(3 << 2 * L) # Remove last 2

            if bitmask in seen:
                res.add(s[i-9:i+1])

            seen.add(bitmask)

        return res
        
